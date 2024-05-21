from bottle import post, get, request, response, template
import os
import uuid
import time
import dbconnection

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  
UPLOADS_FOLDER = os.path.join(ROOT_DIR, "uploads") 

def save_file(upload):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    if upload and upload.filename:
        file_extension = upload.filename.split('.')[-1].lower()
        if file_extension in allowed_extensions:
            os.makedirs(UPLOADS_FOLDER, exist_ok=True)

            file_name = str(uuid.uuid4()) + '.' + file_extension
            file_path = os.path.join(UPLOADS_FOLDER, file_name)  

            with open(file_path, "wb") as open_file:
                open_file.write(upload.file.read())

            return "/uploads/" + file_name
    return None  


def get_current_user():
    try:
        user_info = request.get_cookie('user', secret=os.getenv('MY_SECRET'))
        if not user_info:
            return None
        
        username = user_info.get('username')
        if username:
            db = dbconnection.db()
            current_user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            db.close()
            return current_user
        else:
            return None
    except Exception as e:
        print(e)
        return None

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

        db = dbconnection.db()
        cursor = db.cursor()

        cursor.execute("""
            INSERT INTO messages (message_id, user_id, message_subject, message_text, message_file, created_at, deleted_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (message_id, user_id, message_subject, message_text, file_path, created_at, deleted_at))

        db.commit()

        return {"info": "Beskeden er blevet sendt."}

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
        db = dbconnection.db()
        return template("messages.html")
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()


@get("/admin_messages")
def admin_messages_get():
    try:
        db = dbconnection.db()
        
        cursor = db.cursor()
        cursor.execute("""
            SELECT 
                messages.message_id,
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
        
        return template("admin_messages.html", messages=messages)
    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
        return {"info": str(e)}
    finally:
        if "db" in locals():
            db.close()


@post('/delete_message')
def delete_message():
    try:
        message_id = request.forms.get('message_id')
        if not message_id:
            response.status = 400
            return {"info": "Besked-ID mangler"}

        current_user = get_current_user()
        if not current_user:
            response.status = 401
            return {"info": "Bruger ikke logget ind"}
        
        user_id = current_user['user_id']

        deleted_at = int(time.time())

        db = dbconnection.db()
        cursor = db.cursor()

        cursor.execute("""
            UPDATE messages 
            SET deleted_at = ?
            WHERE message_id = ? AND user_id = ?
        """, (deleted_at, message_id, user_id))

        db.commit()

        if cursor.rowcount == 0:
            response.status = 404
            return {"info": "Besked ikke fundet"}

        return {"info": "Besked slettet"}

    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
        return {"info": str(e)}

    finally:
        if "db" in locals():
            db.close()
