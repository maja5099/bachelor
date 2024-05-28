from bottle import post, request, get, response, template
import master
import uuid
import time
import bcrypt

@post("/signup")
def _():
    try:
        db = master.db()
        user_id = str(uuid.uuid4().hex)
        first_name = request.forms.get("first_name")
        last_name = request.forms.get("last_name")
        email = master.validate_email()
        phone = master.validate_phone()
        username = master.validate_username()
        password = master.validate_password()
        is_active = "True"
        created_at = int(time.time())
        updated_at = int(time.time())
        deleted_at = ""
        website_name = request.forms.get("website_name", "")
        website_url = request.forms.get("website_url", "")

       
        staff_emails = ["kontakt@unidstudio.dk", "denise@unidstudio.dk", "isabella@unidstudio.dk"]
        if email in staff_emails:
            user_roles_user_role_id = "2" 
            staff_id = user_id  
            db.execute("INSERT INTO staff (staff_id, user_role_id) VALUES (?, ?)", (staff_id, user_roles_user_role_id))
        else:
            user_roles_user_role_id = "1" 
            customer_id = user_id  
            db.execute("INSERT INTO customers (customer_id, user_role_id, website_name, website_url) VALUES (?, ?, ?, ?)", (customer_id, user_roles_user_role_id, website_name, website_url))

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
            "user_roles_user_role_id" : user_roles_user_role_id,
        }


        db.execute("INSERT INTO users (user_id, first_name, last_name, email, phone, username, password, is_active, created_at, updated_at, deleted_at, user_roles_user_role_id) VALUES (:user_id, :first_name, :last_name, :email, :phone, :username, :password, :is_active, :created_at, :updated_at, :deleted_at, :user_roles_user_role_id)", user)

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
        return template("signup.html")
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
