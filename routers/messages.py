from bottle import post, get, request, response, template, delete, route
import os
import uuid
import time
import master
from math import floor
from datetime import datetime
from common.get_current_user import get_current_user
from common.find_template import find_template, template_dirs


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
UPLOADS_FOLDER = os.path.join(ROOT_DIR, "uploads") 


# upload=None solves missing 1 required positional argument: 'upload' error
def save_file(upload=None):
    if upload and upload.filename:
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        file_extension = upload.filename.split('.')[-1].lower()
        if file_extension in allowed_extensions:
            os.makedirs(UPLOADS_FOLDER, exist_ok=True)
            file_name = str(uuid.uuid4()) + '.' + file_extension
            file_path = os.path.join(UPLOADS_FOLDER, file_name)  
            with open(file_path, "wb") as open_file:
                open_file.write(upload.file.read())
            return "/uploads/" + file_name
    return None
 

 ##############################
#   Converts minutes to hours and minutes
def minutes_to_hours_minutes(minutes):
    hours = floor(minutes / 60)
    remaining_minutes = minutes % 60
    return hours, remaining_minutes


##############################
#   Adds minutes and hours depending on the time
def format_time_spent(minutes):
    if minutes <= 60:
        return f"{minutes} minutter"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours} timer og {remaining_minutes} minutter"


##############################
#   Formats timestamp
def format_created_at(timestamp):
    if isinstance(timestamp, str):
        try:
            timestamp = int(timestamp)
        except ValueError:
            print("Fejl: Timestamp kan ikke konverteres til en integer.")
            return None
    created_at_dt = datetime.fromtimestamp(timestamp)
    formatted_created_at = created_at_dt.strftime('%d-%m-%Y %H:%M')
    return formatted_created_at


@post('/send_message')
def send_message():
    try:
        message_subject = request.forms.get('subject')
        message_text = request.forms.get('message')
        message_file = request.files.get('file')

        if not message_subject or not message_text:
            response.status = 400
            return {"info": "Emne og beskedtekst er påkrævet"}

        file_path = save_file(message_file)

        if file_path is None:
            file_path = "" 

        message_id = str(uuid.uuid4().hex)

        current_user = get_current_user()
        if not current_user:
            response.status = 401
            return {"info": "Bruger ikke logget ind"}
        user_id = current_user['user_id']

        created_at = int(time.time())
        deleted_at = ""

        db = master.db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO messages (message_id, user_id, message_subject, message_text, message_file, created_at, deleted_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (message_id, user_id, message_subject, message_text, file_path, created_at, deleted_at))

        db.commit()

        return {"info": "Beskeden er blevet sendt!"}

    except ValueError as ve:
        response.status = 400
        return {"info": str(ve)}
    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
        response.status = 500
        return {"info": str(e)}

    finally:
        if "db" in locals():
            db.close()


@get("/messages")
def messages_get():
    try:
        db = master.db()
        template_path = find_template('profile_customer_messages', template_dirs)
        if template_path is None:
            return "Template not found."
            
        # Extract the relative path from views directory if necessary
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        return template(relative_path)
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()


@get('/profile/profile_admin_messages')
def admin_messages_get():
    try:
        db = master.db()
        cursor = db.cursor()
        cursor.execute("""
            SELECT 
                messages.message_id,
                messages.created_at,
                messages.message_subject, 
                messages.message_text, 
                messages.message_file,
                users.first_name, 
                users.last_name, 
                customers.website_name,
                customers.website_url
            FROM messages
            JOIN users ON messages.user_id = users.user_id
            JOIN customers ON messages.user_id = customers.customer_id
            WHERE messages.deleted_at IS ""
            ORDER BY messages.created_at DESC;
        """)

        messages = cursor.fetchall()
        print(messages)

        #   Formats created_at in
        formatted_messages = []
        for message in messages:
            message['formatted_created_at'] = format_created_at(message['created_at'])
            formatted_messages.append(message)

        template_path = find_template('profile_admin_messages', template_dirs)
        if template_path is None:
            return "Template not found."
            
        # Extract the relative path from views directory if necessary
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        return template(relative_path, messages=messages)

    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
        return {"info": str(e)}
    finally:
        if "db" in locals():
            db.close()


@delete('/delete_message')
def delete_message():
    try:
        message_id = request.forms.get('message_id')
        if not message_id:
            response.status = 400
            return {"info": "Message ID is missing."}

        current_user = get_current_user()
        if not current_user:
            response.status = 401
            return {"info": "User not logged in."}
        
        deleted_at = int(time.time())

        db = master.db()
        cursor = db.cursor()

        cursor.execute("""
            UPDATE messages 
            SET deleted_at = ?
            WHERE message_id = ? 
        """, (deleted_at, message_id))

        db.commit()

        if cursor.rowcount == 0:
            response.status = 404
            return {"info": "Message not found."}

        return {"info": "Message deleted."}

    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
        return {"info": str(e)}

    finally:
        if "db" in locals():
            db.close()


