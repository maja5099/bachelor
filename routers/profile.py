from bottle import request, redirect, template, get, route
import os
import master
import content
import logging
from colored_logging import setup_logger
import routers.messages as messages
from math import floor
from datetime import datetime


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


##############################
#   List of directories to search for templates
template_dirs = ['components', 'elements', 'sections', 'utilities']


##############################
#   Get current user
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
            return current_user
        else:
            return None
    except Exception as e:
        print(e)
        return None


##############################
#   Converts minutes to hours and minutes
def minutes_to_hours_minutes(minutes):
    hours = floor(minutes / 60)
    remaining_minutes = minutes % 60
    return hours, remaining_minutes


##############################
#   Adds minutes and hours depending on the time
def format_time_spent(minutes):
    if minutes <= 60:
        return f"{minutes} minutter"
    else:
        hours = minutes // 60
        remaining_minutes = minutes % 60
        return f"{hours} timer og {remaining_minutes} minutter"


##############################
#   Formats timestamp
def format_created_at(timestamp):
    if isinstance(timestamp, str):
        try:
            timestamp = int(timestamp)
        except ValueError:
            print("Fejl: Timestamp kan ikke konverteres til en integer.")
            return None
    created_at_dt = datetime.fromtimestamp(timestamp)
    formatted_created_at = created_at_dt.strftime('%d-%m-%Y %H:%M')
    return formatted_created_at


##############################
#   Fetching information to be included in the admin/customer profile
def load_profile_data():
    current_user = get_current_user()
    if not current_user:
        logger.info("No current user found, redirecting to login.")
        redirect("/login")

    db = master.db()
    user = current_user

    first_name = user['first_name']
    last_name = user['last_name']
    username = user['username']

    #   Fetching clipcard_id from payments
    payment_query = """
        SELECT payments.clipcard_id
        FROM payments
        JOIN clipcards ON payments.clipcard_id = clipcards.clipcard_id
        WHERE payments.user_id = ? AND clipcards.is_active = 1
        LIMIT 1
    """
    payment = db.execute(payment_query, (user['user_id'],)).fetchone()

    #   Fetching time_used and remaining_time from active clipcards
    if payment:
        clipcard_id = payment['clipcard_id']
        
        clipcard_query = """
            SELECT time_used, remaining_time
            FROM clipcards
            WHERE clipcard_id = ? AND is_active = 1
        """
        clipcard_data = db.execute(clipcard_query, (clipcard_id,)).fetchone()

        #   Converts time_used and remaining_time to hours and minutes
        if clipcard_data:
            time_used = clipcard_data['time_used']
            remaining_time = clipcard_data['remaining_time']
            time_used_hours, time_used_minutes = minutes_to_hours_minutes(time_used)
            remaining_hours, remaining_minutes = minutes_to_hours_minutes(remaining_time)
        else:
            logger.info("Clipcard data not found or inactive for user.")
            time_used_hours = None
            time_used_minutes = None
            remaining_hours = None
            remaining_minutes = None
    else:
        logger.info("Payment not found for user.")
        time_used_hours = None
        time_used_minutes = None
        remaining_hours = None
        remaining_minutes = None

    #   Fetching active and inactive clipcards
    active_clipcards_result = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 1").fetchone()
    inactive_clipcards_result = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 0").fetchone()

    active_clipcards_count = active_clipcards_result['count']
    inactive_clipcards_count = inactive_clipcards_result['count']

    #   Fetching tasks
    tasks_query = """
        SELECT task_title, task_description, time_spent, created_at
        FROM tasks
        WHERE customer_id = ?
        ORDER BY created_at DESC
    """
    tasks = db.execute(tasks_query, (user['user_id'],)).fetchall()

    #   Formats time_spent and created_at in tasks
    formatted_tasks = []
    for task in tasks:
        task['formatted_time_spent'] = format_time_spent(task['time_spent'])
        task['formatted_created_at'] = format_created_at(task['created_at'])
        formatted_tasks.append(task)

    return {
        'user': user,
        'first_name': first_name,
        'last_name': last_name,
        'username': username,
        'active_clipcards_count': active_clipcards_count,
        'inactive_clipcards_count': inactive_clipcards_count,
        'time_used_hours': time_used_hours,
        'time_used_minutes': time_used_minutes,
        'remaining_hours': remaining_hours,
        'remaining_minutes': remaining_minutes,
        'tasks': formatted_tasks
    }


##############################
#   Get user profile
@get("/profile")
def profile():
    try:
        data = load_profile_data()

        return template('profile', title="Din profil",
                        user=data['user'],
                        pricing_default=pricing_default,
                        pricing_accent=pricing_accent,
                        section_profile_admin=section_profile_admin,
                        section_profile_customer=section_profile_customer,
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        header_nav_items=header_nav_items,
                        footer_info=footer_info,
                        unid_logo=unid_logo,
                        selling_points=selling_points,
                        social_media=social_media,
                        ui_icons=ui_icons,
                        active_clipcards_count=data['active_clipcards_count'],
                        inactive_clipcards_count=data['inactive_clipcards_count'],
                        time_used_hours=data['time_used_hours'],
                        time_used_minutes=data['time_used_minutes'],
                        remaining_hours=data['remaining_hours'],
                        remaining_minutes=data['remaining_minutes'],
                        tasks=data['tasks'])

    except Exception as e:
        logger.error("Error loading profile: %s", e)
    finally:
        logger.info("Profile request completed.")


##############################
#   Get user profile and template
@route('/profile/<template_name>')
def profile_template(template_name):
    logger.info(f"Request for template: {template_name}")
    try:
        #   Include profile data if the template is profile_overview
        data = load_profile_data()
        if template_name == "profile_overview":
            template_path = find_template(template_name, template_dirs)
            if template_path is None:
                return "Template not found."
            relative_path = template_path.replace('views/', '').replace('.tpl', '')

            logger.info("Variables before rendering template: active_clipcards_count=%s, inactive_clipcards_count=%s", data['active_clipcards_count'], data['inactive_clipcards_count'])

            return template(relative_path,
                            user=data['user'],
                            first_name=data['first_name'],
                            last_name=data['last_name'],
                            username=data['username'],
                            ui_icons=ui_icons,
                            active_clipcards_count=data['active_clipcards_count'],
                            inactive_clipcards_count=data['inactive_clipcards_count'],
                            time_used_hours=data['time_used_hours'],
                            time_used_minutes=data['time_used_minutes'],
                            remaining_hours=data['remaining_hours'],
                            remaining_minutes=data['remaining_minutes'],
                            tasks=data['tasks'])
        else:
            # General template logic
            template_path = find_template(template_name, template_dirs)
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
                            user=data['user'], 
                            pricing_default=pricing_default, 
                            pricing_accent=pricing_accent, 
                            section_profile_admin=section_profile_admin, 
                            section_profile_customer=section_profile_customer, 
                            first_name=data['first_name'], 
                            last_name=data['last_name'], 
                            username=data['username'], 
                            header_nav_items=header_nav_items, 
                            footer_info=footer_info, 
                            unid_logo=unid_logo, 
                            selling_points=selling_points, 
                            social_media=social_media, 
                            ui_icons=ui_icons)
    except Exception as e:
        logger.error("Error loading template '%s': %s", template_name, e)
        return f"Error loading template {template_name}: {e}"
    finally:
        logger.info("Template request for '%s' completed.", template_name)

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
