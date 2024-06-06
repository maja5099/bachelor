from bottle import post, request, response, template, get
import master
import bcrypt
import os
from dotenv import load_dotenv
import content

##############################
# Content from content.py
form_inputs = content.form_inputs
unid_logo = content.unid_logo
section_login_content = content.section_login_content

def set_cookie_secure(cookie_name, cookie_value):
    host = os.getenv('HOST')
    if host != 'localhost':
        response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=True, secure=True, samesite='Strict')
    else:
        response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=True)

def set_csrf_cookie_secure(cookie_name, cookie_value):
    host = os.getenv('HOST')
    if host != 'localhost':
        response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=False, secure=True, samesite='Strict')
    else:
        response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=False)

@post("/login")
def login():
    try:
        load_dotenv('.env')
        
        username = request.forms.get("username")
        password = request.forms.get("password")
        csrf_token = request.forms.get("csrf_token") 

        # Check if CSRF token is valid
        if csrf_token != request.get_cookie("csrf_token", secret=os.getenv('MY_SECRET')):
            response.status = 400
            raise Exception("Invalid CSRF token")

        if not username or not password:
            response.status = 400
            raise Exception("You must fill out both username and password to log in.")
            
        db = master.db()
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()

        if not user: 
            response.status = 400
            raise Exception("The username does not exist")
   
        hashed_password_from_db = user["password"]

        if bcrypt.checkpw(password.encode("utf-8"), hashed_password_from_db):
            user.pop("password")
            set_cookie_secure("user", user)

            # Generate a new CSRF token after successful login
            csrf_token = master.generate_csrf_token()
            print("CSRF token:", csrf_token)  
            set_csrf_cookie_secure("csrf_token", csrf_token)

            return {"info": "Login successful", "redirect": "/"}
        else:
            response.status = 400 
            raise Exception("The password is incorrect") 
    
    except Exception as e:
        error_message = str(e)
        print(error_message) 
        return {"error": error_message}
    
    finally:
        if "db" in locals(): 
            db.close()

@get("/login")
def login_get():
    try:
        db = master.db()
        csrf_token = request.forms.get("csrf_token")

        return template("login", title="Log in", form_inputs=form_inputs, section_login_content=section_login_content, unid_logo=unid_logo, csrf_token=csrf_token)
    
    except Exception as e:
        print(e)  
        if "db" in locals(): db.rollback() 
        return {"info": str(e)}
    
    finally:
        if "db" in locals(): db.close()



