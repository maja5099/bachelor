##############################
#   IMPORTS
#   Library imports
from bottle import post, request, template, get, response
from dotenv import load_dotenv
import time
import uuid
import bcrypt
import logging

#   Local application imports
from common.colored_logging import setup_logger
import common.content as content
import master


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
    signup_content = content.signup_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   SIGNUP - POST
@post("/signup")
def signup():

    function_name = "signup"
    response.content_type = 'application/json'

    try:
        # Load environment variables
        load_dotenv('.env')
        logger.info(f"Starting {function_name} request")

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        # Validate inputs
        email_error = master.validate_email()
        phone_error = master.validate_phone()
        username_error = master.validate_username()
        password_error = master.validate_password()

        # Return error messages for invalid inputs
        if email_error:
            logger.error(email_error)
            return {"error": email_error}
        if phone_error:
            logger.error(phone_error)
            return {"error": phone_error}
        if username_error:
            logger.error(username_error)
            return {"error": username_error}
        if password_error:
            logger.error(password_error)
            return {"error": password_error}

        # Retrieve form data
        email = request.forms.get("email")
        phone = request.forms.get("phone")
        username = request.forms.get("username")
        password = request.forms.get("password")
        first_name = request.forms.get("first_name")
        last_name = request.forms.get("last_name")
        website_name = request.forms.get("website_name", "")
        website_url = request.forms.get("website_url", "")

        # Check if email, phone, and username already exists in db (prevent dublicates)
        existing_user_email = db.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
        existing_user_phone = db.execute("SELECT * FROM users WHERE phone = ?", (phone,)).fetchone()
        existing_user_username = db.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

        if existing_user_email:
            logger.error("Email already exists")
            return {"error": "Den indtastede email eksisterer allerede."}
        if existing_user_phone:
            logger.error("Phone already exists")
            return {"error": "Det indtastede telefonnummer eksisterer allerede."}
        if existing_user_username:
            logger.error("Username already exists")
            return {"error": "Det indtastede brugernavn eksisterer allerede."}

        # Generate unique identifiers and timestamps
        user_id = str(uuid.uuid4().hex)
        is_active = 1
        created_at = int(time.time())
        updated_at = int(time.time())
        deleted_at = ""

        # Check if email is staff emails (determines user roles)
        staff_emails = ["kontakt@unidstudio.dk", "denise@unidstudio.dk", "isabella@unidstudio.dk"]
        if email in staff_emails:
            user_role_id = "2"
            staff_id = user_id
            db.execute("INSERT INTO staff (staff_id, user_role_id) VALUES (?, ?)", (staff_id, user_role_id))
        else:
            user_role_id = "1"
            customer_id = user_id
            db.execute("INSERT INTO customers (customer_id, user_role_id, website_name, website_url) VALUES (?, ?, ?, ?)", (customer_id, user_role_id, website_name, website_url))

        # Hash password using bcrypt and salt
        salt = bcrypt.gensalt()
        password_hashed = bcrypt.hashpw(password.encode("utf-8"), salt)

        # Prepare user dictionary for insertion into database
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

        # Insert user data into users table
        db.execute("INSERT INTO users (user_id, first_name, last_name, email, phone, username, password, is_active, created_at, updated_at, deleted_at, user_role_id) VALUES (:user_id, :first_name, :last_name, :email, :phone, :username, :password, :is_active, :created_at, :updated_at, :deleted_at, :user_role_id)", user)

        # Commit changes to the database
        db.commit()
        logger.success(f"{function_name} successful")
        return {"message": f"{function_name} successful"}

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {function_name}: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {function_name}")


##############################
#   SIGNUP - GET
@get("/signup")
def signup_get():

    page_name = "signup"

    try:
        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name,
                        title="Sign up",
                        # A-Z
                        global_content=global_content,
                        signup_content=signup_content
                        )

    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        logger.info(f"Completed request for /{page_name}")
