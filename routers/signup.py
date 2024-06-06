from bottle import post, request, get, response, template
import master
import uuid
import time
import bcrypt
import os

def set_csrf_cookie_secure(cookie_name, cookie_value):
    host = os.getenv('HOST')
    if host != 'localhost':
        response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=False, secure=True, samesite='Strict')
    else:
        response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=False)

@post("/signup")
def _():
    try:
        db = master.db()

        # Get the CSRF token from the form sent with the POST request
        csrf_token_post = request.forms.get("csrf_token")
        
        # Get the CSRF token from the cookie
        csrf_token_cookie = request.get_cookie("csrf_token", secret=os.getenv('MY_SECRET'))
        
        # Verify CSRF token
        if csrf_token_post != csrf_token_cookie:
            raise Exception("Invalid CSRF token")

        user_id = str(uuid.uuid4().hex)
        first_name = request.forms.get("first_name")
        last_name = request.forms.get("last_name")
        email = master.validate_email()
        phone = master.validate_phone()
        username = master.validate_username()
        password = master.validate_password()
        is_active = 1
        created_at = int(time.time())
        updated_at = int(time.time())
        deleted_at = ""
        website_name = request.forms.get("website_name", "")
        website_url = request.forms.get("website_url", "")

        staff_emails = ["kontakt@unidstudio.dk", "denise@unidstudio.dk", "isabella@unidstudio.dk"]
        if email in staff_emails:
            user_role_id = "2" 
            staff_id = user_id  
            db.execute("INSERT INTO staff (staff_id, user_role_id) VALUES (?, ?)", (staff_id, user_role_id))
        else:
            user_role_id = "1" 
            customer_id = user_id  
            db.execute("INSERT INTO customers (customer_id, user_role_id, website_name, website_url) VALUES (?, ?, ?, ?)", (customer_id, user_role_id, website_name, website_url))

        salt = bcrypt.gensalt()

        user = {
            "user_id" : user_id,
            "username" : username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password" : bcrypt.hashpw(password.encode("utf-8"), salt),
            "is_active" : is_active,
            "created_at" : created_at,
            "updated_at" : updated_at,
            "deleted_at" : deleted_at,
            "user_role_id" : user_role_id,
        }

        db.execute("INSERT INTO users (user_id, first_name, last_name, email, phone, username, password, is_active, created_at, updated_at, deleted_at, user_role_id) VALUES (:user_id, :first_name, :last_name, :email, :phone, :username, :password, :is_active, :created_at, :updated_at, :deleted_at, :user_role_id)", user)

        db.commit()

        return {"info": "Signup succesful!"}
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback()
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()

@get("/signup")
def signup_get():
    try:
        db = master.db()
        
        # Generer et CSRF-token
        csrf_token = master.generate_csrf_token()

        # Udskriv værdien af CSRF-tokenet og sæt det i cookien
        print("CSRF token (GET):", csrf_token)
        set_csrf_cookie_secure("csrf_token", csrf_token)

        return template("signup.html", csrf_token=csrf_token)
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
