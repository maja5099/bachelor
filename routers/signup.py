from bottle import post, request, get, response, template
import dbconnection
import uuid
import time
import bcrypt

@post("/signup")
def _():
    try:
        db = dbconnection.db()
        user_id = str(uuid.uuid4().hex)
        first_name = request.forms.get("first_name", "")
        last_name = request.forms.get("last_name", "")
        email = dbconnection.validate_email()
        phone = dbconnection.validate_phone()
        username = dbconnection.validate_username()
        password = dbconnection.validate_password()
        is_active = "True"
        created_at = int(time.time())
        updated_at = int(time.time())
        deleted_at = ""
        website_name = request.forms.get("website_name", "")
        website_url = request.forms.get("website_url", "")

        # Bestemmer brugerens rolle baseret på deres e-mail-adresse
        staff_emails = ["kontakt@unidstudio.dk", "denise@unidstudio.dk", "isabella@unidstudio.dk"]
        if email in staff_emails:
            user_roles_user_role_id = "2"  # ID for staff role
            staff_id = str(uuid.uuid4().hex)  # Generer staff_id
            # Indsæt brugeren i staff-tabellen
            db.execute("INSERT INTO staff (staff_id, user_role_id) VALUES (?, ?)", (staff_id, user_roles_user_role_id))
        else:
            user_roles_user_role_id = "1"  # ID for customer role
            customer_id = str(uuid.uuid4().hex)  # Generer customer_id
            # Indsæt brugeren i customers-tabellen
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

        # Indsæt brugeren i users-tabellen
        db.execute("INSERT INTO users (user_id, first_name, last_name, email, phone, username, password, is_active, created_at, updated_at, deleted_at, user_roles_user_role_id) VALUES (:user_id, :first_name, :last_name, :email, :phone, :username, :password, :is_active, :created_at, :updated_at, :deleted_at, :user_roles_user_role_id)", user)
        
        # Commit ændringer til databasen
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
        db = dbconnection.db()
        return template("signup.html")
    except Exception as e:
        print(e)
        if "db" in locals(): db.rollback() 
        return {"info":str(e)}
    finally:
        if "db" in locals(): db.close()
