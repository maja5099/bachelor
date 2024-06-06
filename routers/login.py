##############################
#   IMPORTS
#   Library imports
from bottle import post, request, response, template, get
from dotenv import load_dotenv
import bcrypt
import logging
import os

#   Local application imports
from colored_logging import setup_logger
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
    ui_icons = content.ui_icons
    unid_logo = content.unid_logo
    # Content for this page
    section_login_content = content.section_login_content
    form_inputs=content.form_inputs
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#  SET COOKIE
def set_cookie_secure(cookie_name, cookie_value):
    try:
        host = os.getenv('HOST')
        logger.success(f"Successfully set cookie: {cookie_name}")
        if host != 'localhost':
            response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=True, secure=True, samesite='Strict')
            logger.info(f"Set secure cookie {cookie_name} with strict policies.")
        else:
            response.set_cookie(cookie_name, cookie_value, secret=os.getenv('MY_SECRET'), httponly=True)
            logger.info(f"Set cookie {cookie_name} with httponly.")

    except Exception as e:
        logger.error(f"Error setting cookie {cookie_name}. Error: {e}")
        raise

    finally:
        logger.info(f"Process of setting cookie {cookie_name} completed.")


##############################
#   LOGIN - POST
@post("/login")
def login():

    page_name = "login"

    try:
        load_dotenv('.env')
        logger.info(f"Starting login request")
        
        username = request.forms.get("username")
        password = request.forms.get("password")
    
        if not username or not password:
            logger.warning("Both username and password must be filled out")
            return {"error": "Både brugernavn og adgangskode skal udfyldes"}
        
        db = master.db()
        logger.debug("Database connection opened for login")
        
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
        if not user:
            logger.error("User does not exist")
            return {"error": "Brugernavnet eksisterer ikke"}
        
        hashed_password_from_db = user["password"]
        if bcrypt.checkpw(password.encode("utf-8"), hashed_password_from_db):
            user.pop("password")
            set_cookie_secure("user", user)
            logger.success(f"Login successful for user {username}. Redirected user.")
            return {"info": "Login successful", "redirect": "/"}
        
        else:
            logger.error("Incorrect password")
            return {"error": "Adgangskoden er forkert"}
    
    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /{page_name}: {e}")
        raise
    
    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for /{page_name}")



##############################
#   LOGIN - GET
@get("/login")
def login_get():

    page_name = "login"

    try:
        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name, 
                    title="Log in", 
                    form_inputs=form_inputs, 
                    section_login_content=section_login_content, 
                    unid_logo=unid_logo
                    )
    
    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        logger.info(f"Completed request for /{page_name}")