from bottle import post, request, response, redirect, template, get
import bcrypt
import os
from dotenv import load_dotenv
import master
import content



##############################
#   Content from content.py
form_inputs = content.form_inputs
unid_logo = content.unid_logo
section_login_content = content.section_login_content



from bottle import post, request, response
import bcrypt
import os
from dotenv import load_dotenv

@post("/login")
def _():
    try:
        load_dotenv('.env')


        username = request.forms.get("username")
        password = request.forms.get("password")

        if not username or not password:
            response.status = 400
            raise Exception("Du skal udfylde både brugernavn og adgangskode, for at logge ind.")
            
        db = master.db()
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()

        if not user: 
            response.status = 400
            raise Exception("Brugernavnet eksisterer ikke")
   
        hashed_password_from_db = user["password"]

        if bcrypt.checkpw(password.encode("utf-8"), hashed_password_from_db):
            user.pop("password")
            response.set_cookie("user", user, secret=os.getenv('MY_SECRET'), httponly=True, Secure=True, samesite='Strict')
            return {"info": "Login successful", "redirect": "/"}
        else:
            response.status = 400 
            raise Exception("Adgangskoden er forkert") 
    
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
        return template("login", title="Log ind", form_inputs=form_inputs, section_login_content=section_login_content,unid_logo=unid_logo)
    
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    
    finally:
        if "db" in locals(): db.close()
