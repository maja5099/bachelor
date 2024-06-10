##############################
#   IMPORTS
#   Library imports
from bottle import post, redirect, response, request
import logging
import os

#   Local application imports
from common.colored_logging import setup_logger
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
#   LOGOUT
@post("/logout")
def logout():

    function_name = "logout"

    try:
        # Securely retrieve user cookie
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))

        if not user_cookie:
            logger.info("No user cookie found, no user to log out")
            return redirect("/")

        # Database connection and user validation
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")
        user = db.execute("SELECT * FROM users WHERE username = ?", (user_cookie['username'],)).fetchone()

        # Handle user not found in the database
        if not user:
            logger.error(f"User not found in database: {user_cookie['username']}")
            return redirect("/")

        # User and cookie found, perform logout
        username = user['username']
        logger.info(f"Attempting to log out user: {username}")
        response.delete_cookie("user")
        logger.success(f"Successfully logged out user: {username}")
        return redirect("/")
    
    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {function_name} of user {username}. Error: {e}")
        raise
    
    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for {function_name}")
