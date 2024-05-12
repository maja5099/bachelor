from bottle import post, request, response, redirect, template, get
import bcrypt
import os
from dotenv import load_dotenv
import dbconnection

form_inputs = {
    "username": {
        "label_for": "username",
        "text": "Brugernavn", 
        "icon": "user_circle.tpl", 
        "type": "text",
        "name": "username",
        "inputmode":"text",
        "placeholder": "LoremIpsum",
        "form_info": "",
    },
    "password": {
        "label_for": "pwd",
        "text": "Adgangskode", 
        "icon": "lock.tpl", 
        "type": "password",
        "name": "pwd",
        "inputmode":"text",
        "placeholder": "••••••••",
        "form_info": "Use at least 8 characters, one uppercase, one lowercase and one number.",
    },
    "fname": {
        "label_for": "fname",
        "text": "Fornavn", 
        "icon": "user_name_semi.tpl", 
        "type": "text",
        "name": "fname",
        "inputmode":"text",
        "placeholder": "Lorem",
        "form_info": "",    
    },
    "lname": {
        "label_for": "lname",
        "text": "Efternavn", 
        "icon": "user_name_full.tpl", 
        "type": "text",
        "name": "lname",
        "inputmode":"text",
        "placeholder": "Ipsum",
        "form_info": "",    
    },
    "email": {
        "label_for": "email",
        "text": "Email", 
        "icon": "email.tpl", 
        "type": "email",
        "name": "email",
        "inputmode":"email",
        "placeholder": "loremipsum@mail.com",
        "form_info": "",    
    },
    "phone": {
        "label_for": "phone",
        "text": "Telefon nummer", 
        "icon": "phone.tpl", 
        "type": "tel",
        "name": "phone",
        "inputmode":"tel",
        "placeholder": "12 34 56 67",
        "form_info": "",    
    },
    "website_name": {
        "label_for": "website_name",
        "text": "Navn på din hjemmeside", 
        "icon": "pen_line.tpl", 
        "type": "text",
        "name": "website_name",
        "inputmode":"text",
        "placeholder": "Lorem-Ipsum.dk",
        "form_info": "",    
    },
    "website_url": {
        "label_for": "website_url",
        "text": "URL til din hjemmeside", 
        "icon": "www.tpl", 
        "type": "url",
        "name": "website_url",
        "inputmode":"url",
        "placeholder": "https://www.lorem-ipsum.dk",
        "form_info": "",    
    },
}

section_login_content = {
    "header_text": "Log ind",
    "subheader_text": "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quae, voluptatum!",
    "error_icon": "exclamation_mark.tpl",
    "button_text": "Log ind",
    "image": "unid_universe.svg",
    "logo": "primary_logo.svg",
}

@post("/login")
def _():
    try:
        load_dotenv('.env')

        username = request.forms.get("username")
        password = request.forms.get("password")

        if not username or not password:
            response.status = 400
            raise Exception("Du skal udfylde både brugernavn og adgangskode, for at logge ind.")
            

        db = dbconnection.db()
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()

        if not user: 
            response.status = 400
            raise Exception("Brugernavnet eksisterer ikke")
   
        hashed_password_from_db = user["password"]
        hashed_password_input = bcrypt.hashpw(password.encode("utf-8"), hashed_password_from_db)

        if hashed_password_input == hashed_password_from_db:
            user.pop("password")
            response.set_cookie("user", user, secret=os.getenv('MY_SECRET'), httponly=True)
            return redirect("/")
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
        db = dbconnection.db()
        return template("login", title="Log ind", form_inputs=form_inputs, section_login_content=section_login_content)
    
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    
    finally:
        if "db" in locals(): db.close()