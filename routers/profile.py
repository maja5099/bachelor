from bottle import request, redirect, template, get, route
import os
import master
import content
import logging
from colored_logging import setup_logger
import routers.messages as messages



##############################
#   COLORED LOGGING
logger = setup_logger(__name__, level=logging.INFO)
logger.setLevel(logging.INFO)


##############################
#   Content from content.py
try:
    header_nav_items = content.header_nav_items
    footer_info = content.footer_info
    unid_logo = content.unid_logo
    selling_points = content.selling_points
    social_media = content.social_media
    ui_icons = content.ui_icons
    pricing_default = content.pricing_default
    pricing_accent = content.pricing_accent
    section_profile_admin = content.section_profile_admin
    section_profile_customer = content.section_profile_customer
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error("Error importing content: %s", e)
finally:
    logger.info("Content import process completed.")


# List of directories to search for templates
template_dirs = ['components', 'elements', 'sections', 'utilities']


@get("/profile")
def profile():
    try:
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        if not user_cookie:
            logger.info("No user cookie found, redirecting to login.")
            redirect("/login")

        db = master.db()
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (user_cookie['username'],)).fetchone()
        
        if not user:
            logger.info("User not found in database, redirecting to login.")
            redirect("/login")

        first_name = user['first_name']
        last_name = user['last_name']
        username = user['username']
        logger.success("User profile loaded successfully: %s", username)

        return template('profile', 
                        title="Din profil", 
                        user=user, 
                        pricing_default=pricing_default, 
                        pricing_accent=pricing_accent, 
                        section_profile_admin=section_profile_admin, 
                        section_profile_customer=section_profile_customer, 
                        first_name=first_name, 
                        last_name=last_name, 
                        username=username, 
                        header_nav_items=header_nav_items, 
                        footer_info=footer_info, 
                        unid_logo=unid_logo, 
                        selling_points=selling_points, 
                        social_media=social_media, 
                        ui_icons=ui_icons)
    except Exception as e:
        logger.error("Error loading profile: %s", e)
    finally:
        logger.info("Profile request completed.")

def template_finder(template_name, directories):
    for directory in directories:
        for root, _, files in os.walk(f'views/{directory}'):
            if f'{template_name}.tpl' in files:
                logger.success("Template '%s' found in directory '%s'.", template_name, directory)
                return os.path.join(root, f'{template_name}.tpl')
    logger.error("Template '%s' not found in any directories.", template_name)
    return None

@route('/profile/<template_name>')
def profile_template(template_name):
    logger.info(f"Request for template: {template_name}")
    try:
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        if not user_cookie:
            logger.info("No user cookie found, redirecting to login.")
            redirect("/login")

        db = master.db()
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (user_cookie['username'],)).fetchone()

        if not user:
            logger.info("User not found in database, redirecting to login.")
            redirect("/login")

        first_name = user['first_name']
        last_name = user['last_name']
        username = user['username']
        logger.success("User profile for template '%s' loaded successfully: %s", template_name, username)

        # Find correct template
        template_path = template_finder(template_name, template_dirs)
        if template_path is None:
            raise Exception(f"Template '{template_name}' not found in any of the directories.")
        template_path = template_path.replace('views/', '').replace('.tpl', '')

        logger.info(f"Serving template: {template_path}")

        return template(template_path, 
                        title="Din profil", 
                        save_file=messages.save_file,
                        get_current_user=messages.get_current_user,
                        send_message=messages.send_message,
                        messages_get=messages.messages_get,
                        admin_messages_get=messages.admin_messages_get,
                        delete_message=messages.delete_message,
                        user=user, 
                        pricing_default=pricing_default, 
                        pricing_accent=pricing_accent, 
                        section_profile_admin=section_profile_admin, 
                        section_profile_customer=section_profile_customer, 
                        first_name=first_name, 
                        last_name=last_name, 
                        username=username, 
                        header_nav_items=header_nav_items, 
                        footer_info=footer_info, 
                        unid_logo=unid_logo, 
                        selling_points=selling_points, 
                        social_media=social_media, 
                        ui_icons=ui_icons
                        )
    except Exception as e:
        logger.error("Error loading template '%s': %s", template_name, e)
        return f"Error loading template {template_name}: {e}"
    finally:
        logger.info("Template request for '%s' completed.", template_name)

 # type: ignore