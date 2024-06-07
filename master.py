##############################
#   IMPORTS
#   Library imports
from bottle import request, response
from dotenv import load_dotenv
import secrets
import logging
import sqlite3
import pathlib
import os
import re

#   Local application imports
from colored_logging import setup_logger


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
#   DICT FACTORY
def dict_factory(cursor, row):
  col_names = [col[0] for col in cursor.description]
  return {key: value for key, value in zip(col_names, row)}


##############################
#   DB
def db():
    try:
        db_path = str(pathlib.Path(__file__).parent.resolve()) + "/uniduniverse.db"
        db = sqlite3.connect(db_path)
        db.row_factory = dict_factory
        logger.success("Database connection established successfully.")
        return db
    except Exception as e:
        logger.error(f"Error establishing database connection: {e}")
        raise
    finally:
        logger.info("Database function execution completed.")


##############################
#   USER
def user():
    try:
        load_dotenv(".env")
        user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        if user:
            logger.success("User successfully retrieved from cookie.")
            return user
        else:
            logger.warning("No user found in cookie.")
            return None
    except Exception as ex:
        logger.error(f"Error retrieving user from cookie: {ex}")
        raise
    finally:
        logger.info("User function completed.")
    

##############################
#   VALIDATION - EMAIL
EMAIL_MIN = 6
EMAIL_MAX = 100
EMAIL_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_email():
    try:
        error = "User email is not valid"
        email = request.forms.get("email", "").strip()
        if len(email) < EMAIL_MIN:
            response.status = 400
            logger.warning("Email too short.")
            raise Exception(error)
        if len(email) > EMAIL_MAX:
            response.status = 400
            logger.warning("Email too long.")
            raise Exception(error)
        if not re.match(EMAIL_REGEX, email):
            response.status = 400
            logger.error("Email does not match regex.")
            raise Exception(error)
        logger.info("Email validated successfully.")
        return email
    except Exception as e:
        logger.error(f"Error validating email: {e}")
        raise
    finally:
        logger.info("Email validation process completed.")


##############################
#   VALIDATION - USERNAME
USERNAME_MIN = 4
USERNAME_MAX = 15
USERNAME_REGEX = "^[a-zA-Z0-9_]{4,15}$"

def validate_username():
    try:
        error = "Your username has to be between 4 and 15 lowercase English letters"
        username = request.forms.get("username", "").strip()
        if not re.match(USERNAME_REGEX, username):
            logger.error("Username does not match regex.")
            raise Exception(error)
        logger.info("Username validated successfully.")
        return username
    except Exception as e:
        logger.error(f"Error validating username: {e}")
        raise
    finally:
        logger.info("Username validation process completed.")


##############################
#   VALIDATION - PASSWORD
PASSWORD_MIN = 10
PASSWORD_MAX = 128
PASSWORD_REGEX = "^[a-zA-Z0-9]{10,128}$"

def validate_password():
    try:
        error = "Your password must be between 10 to 128 characters long"
        password = request.forms.get("password", "").strip()
        if len(password) < PASSWORD_MIN or len(password) > PASSWORD_MAX:
            logger.error("Password length is out of bounds.")
            raise Exception(error)
        if not re.match(PASSWORD_REGEX, password):
            logger.error("Password does not match regex.")
            raise Exception(error)
        logger.info("Password validated successfully.")
        return password
    except Exception as e:
        logger.error(f"Error validating password: {e}")
        raise
    finally:
        logger.info("Password validation process completed.")


##############################
#   VALIDATION - PHONE
PHONE_REGEX = "^\d{8}$" 

def validate_phone():
    try:
        error = "Phone number must be exactly 8 digits"
        phone = request.forms.get("phone", "").strip()
        if not re.match(PHONE_REGEX, phone):
            logger.error("Phone does not match regex.")
            raise ValueError(error)
        logger.info("Phone validated successfully.")
        return phone
    except Exception as e:
        logger.error(f"Error validating phone: {e}")
        raise
    finally:
        logger.info("Phone validation process completed.")