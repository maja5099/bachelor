##############################
#   IMPORTS
#   Library imports
from bottle import template, get, request
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
    global_content = content.global_content
    # Header
    header_nav_items = content.header_nav_items
    selling_points = content.selling_points
    # Footer
    footer_info = content.footer_info
    social_media = content.social_media
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   PORTFOLIO
@get("/portfolio")
def portfolio():

    page_name = "portfolio"

    try:
        # Securely retrieve user cookie
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))

        # Validate cookie, then fetch user details from db
        if user_cookie and isinstance(user_cookie, dict):
            db = master.db()
            username = user_cookie.get('username')
            user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            logger.success(f"Valid user cookie found for /{page_name}, retrieved data from database")
            logger.info(f"Logged in user: {username}")

        # Handle scenarios where no valid cookie is found (e.g., user not logged in)
        else:
            user = username = None
            logger.warning(f"No valid user cookie found for /{page_name}, perhaps user is not logged in yet")

        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name, 
                        title="UNID Studio - Services og priser", 
                        footer_info=footer_info, 
                        header_nav_items=header_nav_items, 
                        selling_points=selling_points, 
                        social_media=social_media, 
                        global_content=global_content,
                        user=user, 
                        username=username
                        )
    
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