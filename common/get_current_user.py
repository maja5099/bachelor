##############################
#   IMPORTS
#   Library imports
from bottle import request, response
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
#   GET CURRENT USER
def get_current_user():

    function_name = "get_current_user"

    try:
        # Get user information from cookie
        user_info = request.get_cookie('user', secret=os.getenv('MY_SECRET'))
        if not user_info:
            return None
        
        # Extract username from the user information
        username = user_info.get('username')

        # If username is present
        if username:

            # Establish database connection
            db = master.db()
            logger.debug(f"Database connection opened for {function_name}")

            # Get user details from the database
            current_user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()

            db.close()
            logger.success(f"Executed {function_name} successfully: user was fetcged")
            return current_user
        
        else:
            return None
        
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