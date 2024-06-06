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
    ui_icons = content.ui_icons
    unid_logo = content.unid_logo
    # Header
    header_nav_items = content.header_nav_items
    selling_points = content.selling_points
    # Footer
    footer_info = content.footer_info
    social_media = content.social_media
    # Content for this page
    pricing_default = content.pricing_default
    pricing_accent = content.pricing_accent
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   SERVICES_AND_PRICES
@get("/services_and_prices")
def services_and_prices():

    page_name = "services_and_prices"

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

        return template(page_name, 
                        title="UNID Studio - Services og priser", 
                        footer_info=footer_info, 
                        header_nav_items=header_nav_items, 
                        pricing_default = pricing_default,
                        pricing_accent = pricing_accent,
                        selling_points=selling_points, 
                        social_media=social_media, 
                        ui_icons=ui_icons,
                        unid_logo=unid_logo, 
                        user=user, 
                        username=username
                        )
    
    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise
    
    finally:
        logger.info(f"Completed request for /{page_name}")