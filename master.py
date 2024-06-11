##############################
#   IMPORTS
#   Library imports
from bottle import request, response
from dotenv import load_dotenv
import logging
import sqlite3
import pathlib
import os
import re

#   Local application imports
from common.colored_logging import setup_logger


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
EMAIL_REGEX = "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def validate_email():
    email = request.forms.get("email", "").strip()
    if not re.match(EMAIL_REGEX, email):
        return "Den indtastede email er ikke gyldig."
    return None


##############################
#   VALIDATION - USERNAME
USERNAME_REGEX = "^[a-zA-Z0-9_]{4,15}$"

def validate_username():
    username = request.forms.get("username", "").strip()
    if not re.match(USERNAME_REGEX, username):
        return "Brugernavnet skal være mellem 4 og 15 tegn."
    return None


##############################
#   VALIDATION - PHONE
PHONE_REGEX = "^\\d{8}$" 

def validate_phone():
    phone = request.forms.get("phone", "").strip()
    if not re.match(PHONE_REGEX, phone):
        return "Telefonnummeret skal bestå af 8 cifre."
    return None


##############################
#   VALIDATION - PASSWORD
PASSWORD_REGEX = "^[a-zA-Z0-9]{10,128}$"

def validate_password():
    password = request.forms.get("password", "").strip()
    if not re.match(PASSWORD_REGEX, password):
        return "Adgangskoden skal være mellem 10 og 128 tegn lang."
    return None