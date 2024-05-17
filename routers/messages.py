from bottle import post, get, request, response, template
import os
import uuid
import time
import dbconnection

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOADS_FOLDER = os.path.join(os.path.dirname(ROOT_DIR), "uploads")

def save_file(upload):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    file_extension = upload.filename.split('.')[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValueError("Kun filer af typerne PNG, JPG eller JPEG er tilladt.")

    os.makedirs(UPLOADS_FOLDER, exist_ok=True)

    file_name = str(uuid.uuid4()) + '.' + file_extension
    file_path = os.path.join(UPLOADS_FOLDER, file_name)

    with open(file_path, "wb") as open_file:
        open_file.write(upload.file.read())

    return str(file_path)

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

        file_path = None
        if message_file:
            file_path = save_file(message_file)

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

        return "Beskeden er blevet sendt."

    except ValueError as ve:
        response.status = 400
        return str(ve)
    except Exception as e:
        print(e)
        if "db" in locals():
            db.rollback()
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
