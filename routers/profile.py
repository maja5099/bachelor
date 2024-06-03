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

import traceback

@get("/profile/profile_overview")
def profile_overview():
    logger.info("Attempting to load profile overview...")
    try:
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        logger.info("User cookie: %s", user_cookie)  # Midlertidig logbesked
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

        # Execute queries and log raw results
        active_clipcards_count = db.execute("SELECT COUNT(*) FROM clipcards WHERE is_active = 1").fetchone()
        inactive_clipcards_count  = db.execute("SELECT COUNT(*) FROM clipcards WHERE is_active = 0").fetchone()

        logger.info("Active clipcards count result: %s", active_clipcards_count)
        logger.info("Inactive clipcards count result: %s", inactive_clipcards_count)

        logger.info("Rendering template with counts...")

        template_path = find_template('profile_overview', template_dirs)
        if template_path is None:
            return "Template not found."
            
        # Extract the relative path from views directory if necessary
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        # Log variables before rendering template
        logger.info("Variables before rendering template: active_clipcards_count=%s, inactive_clipcards_count=%s", active_clipcards_count, inactive_clipcards_count)

        return template(relative_path, 
                        user=user,
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        ui_icons=ui_icons,
                        active_clipcards_count=active_clipcards_count,
                        inactive_clipcards_count=inactive_clipcards_count)
        
    except Exception as e:
        logger.error("Error loading profile overview: %s", e)
        logger.error("Traceback: %s", traceback.format_exc())
        return f"An error occurred while loading the profile overview: {e}"
    finally:
        logger.info("Profile overview request completed.")


def find_template(template_name, directories):
    base_path = 'views'
    for directory in directories:
        path = os.path.join(base_path, directory)
        print(f"Checking directory: {path}")
        for root, dirs, files in os.walk(path):
            print(f"Visited {root}")
            if f'{template_name}.tpl' in files:
                template_path = os.path.join(root, template_name + '.tpl')
                print(f"Found template at: {template_path}")
                return template_path
    print("Template not found")
    return None


 # type: ignore


