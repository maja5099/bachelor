from bottle import run, post, get, request, response, template
import os
import uuid
import time
import dbconnection
import pathlib

# Funktion til at gemme filer
def save_file(upload):
    allowed_extensions = {'png', 'jpg', 'jpeg'}
    file_extension = upload.filename.split('.')[-1].lower()
    if file_extension not in allowed_extensions:
        raise ValueError("Kun filer af typerne PNG, JPG eller JPEG er tilladt.")

    save_path = str(pathlib.Path(__file__).parent.resolve()) + "/uploads/"
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = save_path + upload.filename
    with open(file_path, "wb") as open_file:
        open_file.write(upload.file.read())
    return file_path

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
        # Hent data fra formularen
        message_subject = request.forms.get('subject')
        message_text = request.forms.get('message')
        message_file = request.files.get('file')

        file_path = None
        if message_file:
            file_path = save_file(message_file)

        # Generer et unikt message_id
        message_id = str(uuid.uuid4().hex)

        # Hent user_id fra den aktuelle bruger
        current_user = get_current_user()
        if not current_user:
            response.status = 401
            return {"info": "Bruger ikke logget ind"}
        user_id = current_user['user_id']

        # Indsæt current_time som int(time.time())
        created_at = int(time.time())
        deleted_at = ""

        # Opret forbindelse til databasen
        db = dbconnection.db()
        cursor = db.cursor()

        # Indsæt besked i databasen
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

@get('/send_message')
def send_message_form():
    return template("messages.html")

