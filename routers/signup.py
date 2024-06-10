##############################
#   IMPORTS
#   Library imports
from bottle import post, request, template, get, response
from dotenv import load_dotenv
import time
import uuid
import bcrypt
import logging
import json

#   Local application imports
from common.colored_logging import setup_logger
import master
import content


##############################
#   COLORED LOGGING
try:
    logger = setup_logger(__name__, level=logging.INFO)
    logger.setLevel(logging.INFO)
    logger.success("Logging imported successfully.")
except Exception as e:
    logger.error(f"Error importing logging: {e}")
finally:
    logger.info("Logging import process completed.")


##############################
#   CONTENT VARIABLES
try:
    # Global
    global_content = content.global_content
    # Content for this page
    section_signup_content = content.section_signup_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   SIGNUP - POST
@post("/signup")
def signup():
    page_name = "signup"
    response.content_type = 'application/json'
    try:
        load_dotenv('.env')
        logger.info(f"Starting signup request")

        db = master.db()
        logger.debug("Database connection opened for signup")

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
        password_hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        user = {
            "user_id": user_id,
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone": phone,
            "password": password_hashed,
            "is_active": is_active,
            "created_at": created_at,
            "updated_at": updated_at,
            "deleted_at": deleted_at,
            "user_role_id": user_role_id,
        }

        db.execute("INSERT INTO users (user_id, first_name, last_name, email, phone, username, password, is_active, created_at, updated_at, deleted_at, user_role_id) VALUES (:user_id, :first_name, :last_name, :email, :phone, :username, :password, :is_active, :created_at, :updated_at, :deleted_at, :user_role_id)", user)

        db.commit()
        logger.success("Signup successful")
        return json.dumps({"message": "Signup successful"})

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /{page_name}: {e}")
        response.status = 500
        return json.dumps({"error": "Internal Server Error"})

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for /{page_name}")


##############################
#   SIGNUP - GET
@get("/signup")
def signup_get():
    page_name = "signup"
    try:
        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name, 
                    title="Sign up", 
                    global_content=global_content,
                    section_signup_content=section_signup_content, 
                    )
    
    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        logger.info(f"Completed request for /{page_name}")



