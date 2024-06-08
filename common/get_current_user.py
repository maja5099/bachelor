##############################
#   IMPORTS
#   Library imports
from bottle import request
import logging
import os

#   Local application imports
from colored_logging import setup_logger
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
    try:
        user_info = request.get_cookie('user', secret=os.getenv('MY_SECRET'))
        if not user_info:
            return None
        
        username = user_info.get('username')
        if username:
            db = master.db()
            current_user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            db.close()
            logger.success("Fetch current user successfully.")
            return current_user
        else:
            return None
        
    except Exception as e:
        logger.error(f"Failed to fetch current user: {e}")
        return None
    finally:
        logger.info("Get current user process completed.")