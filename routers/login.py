from bottle import post, request, response, run, template, get
import bcrypt
import os
from dotenv import load_dotenv
import dbconnection

@post("/login")
def _():
    try:
        load_dotenv('.env')

        username = request.forms.get("username")
        password = request.forms.get("password")

        db = dbconnection.db()
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()

        if not user: 
            response.status = 400
            raise Exception("Brugernavnet eksisterer ikke")

        # Hent den hashede adgangskode fra databasen
        hashed_password_from_db = user["password"]

        # Hash den indtastede adgangskode
        hashed_password_input = bcrypt.hashpw(password.encode("utf-8"), hashed_password_from_db)

        # Sammenlign de to hashede adgangskoder
        if hashed_password_input == hashed_password_from_db:
            user.pop("password")
            response.set_cookie("user", user, secret=os.getenv('MY_SECRET'), httponly=True)
            return {"info": "Login credentials valid", "User": user["username"]}
        else:
            response.status = 400 
            raise Exception("Forkert adgangskode") 
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
        return template("login.html")
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()