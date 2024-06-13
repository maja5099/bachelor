##############################
#   IMPORTS
#   Library imports
from bottle import post, request, response, template, get
from dotenv import load_dotenv
import bcrypt
import logging
import os

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
    login_content = content.login_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   LOGIN - POST
@post("/login")
def login():

    function_name = "login"
    response.content_type = 'application/json'

    try:
        # Load environment variables
        load_dotenv('.env')
        logger.info(f"Starting {function_name} request")

        # Retrieve username and password from form
        username = request.forms.get("username")
        password = request.forms.get("password")

        # Ensure both username and password are given
        if not username or not password:
            logger.warning("Both username and password must be filled out")
            return {"error": "Både brugernavn og adgangskode skal udfyldes"}

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        # Check if user exists in database
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
        if not user:
            logger.error("User does not exist")
            return {"error": "Brugernavnet eksisterer ikke"}

        # Verify the password
        hashed_password_from_db = user["password"]
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password_from_db):
            user.pop("password")
            response.set_cookie("user", user, secret=os.getenv('MY_SECRET'), httponly=True)
            logger.success(f"{function_name} successful for user {username}. Redirected user.")
            return {"info": f"{function_name} successful", "redirect": "/"}

        else:
            logger.error("Incorrect password")
            return {"error": "Adgangskoden er forkert"}

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /{function_name}: {e}")
        raise

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for /{function_name}")


##############################
#   LOGIN - GET
@get("/login")
def login_get():

    page_name = "login"

    try:
        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name,
                        title="UNID Studio - Log ind",
                        # A-Z
                        global_content=global_content,
                        login_content=login_content
                        )

    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        logger.info(f"Completed request for /{page_name}")
