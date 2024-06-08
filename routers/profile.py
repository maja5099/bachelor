from bottle import redirect, template, get, route
import master
import content
import logging
from colored_logging import setup_logger
import routers.messages as messages
from common.get_current_user import *
from common.find_template import *
from common.time_formatting import *


##############################
#   COLORED LOGGING
logger = setup_logger(__name__, level=logging.INFO)
logger.setLevel(logging.INFO)


##############################
#   Content from content.py
try:
    header_nav_items = content.header_nav_items
    footer_info = content.footer_info
    global_content = content.global_content
    selling_points = content.selling_points
    social_media = content.social_media
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
#   Fetching information to be included in customer clipcards / timeregistration
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
            time_used_hours = 0
            time_used_minutes = 0
            remaining_hours = 0
            remaining_minutes = 0
    else:
        logger.info("Payment not found for user.")
        time_used_hours = 0
        time_used_minutes = 0
        remaining_hours = 0
        remaining_minutes = 0


    #   Fetching active and inactive clipcards
    active_clipcards_result = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 1").fetchone()
    inactive_clipcards_result = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 0").fetchone()

    active_clipcards_count = active_clipcards_result['count']
    inactive_clipcards_count = inactive_clipcards_result['count']

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
    }


##############################
#   Get user profile
@get("/profile")
def profile():
    try:
        data = load_profile_data()
        current_user = get_current_user()

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
                        global_content=global_content,
                        selling_points=selling_points,
                        social_media=social_media,
                        current_user=current_user,
                        active_clipcards_count=data['active_clipcards_count'],
                        inactive_clipcards_count=data['inactive_clipcards_count'],
                        time_used_hours=data['time_used_hours'],
                        time_used_minutes=data['time_used_minutes'],
                        remaining_hours=data['remaining_hours'],
                        remaining_minutes=data['remaining_minutes'])

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
        current_user = get_current_user()

        if template_name == "profile_overview":
            template_path = find_template(template_name, template_dirs)
            if template_path is None:
                return "Template not found."
            
            if current_user:
                user_id = current_user['user_id']
                db = master.db()
                clipcard_id = db.execute("SELECT clipcard_id FROM payments WHERE user_id = ? LIMIT 1", (user_id,)).fetchone()
                if clipcard_id:
                    clipcard_id_value = clipcard_id['clipcard_id']
                    print("Clipcard ID:", clipcard_id_value)
                    
                    # Check if the user has any active clipcards
                    has_active_clipcard_query = """
                    SELECT COUNT(*) AS active_clipcards 
                    FROM clipcards 
                    WHERE clipcard_id IN (
                        SELECT clipcard_id 
                        FROM payments 
                        WHERE user_id = ?) 
                    AND is_active = 1
                    """
                    
                    has_active_clipcard_result = db.execute(has_active_clipcard_query, (user_id,)).fetchone()
                    
                    if has_active_clipcard_result and has_active_clipcard_result['active_clipcards'] > 0:
                        current_user['has_active_clipcard'] = True
                    else:
                        current_user['has_active_clipcard'] = False

            relative_path = template_path.replace('views/', '').replace('.tpl', '')

            print("Current User:", current_user)
            if current_user:
                print("Has active clipcard:", current_user.get('has_active_clipcard'))

            logger.info("Variables before rendering template: active_clipcards_count=%s, inactive_clipcards_count=%s", data['active_clipcards_count'], data['inactive_clipcards_count'])

            return template(relative_path,
                            user=data['user'],
                            first_name=data['first_name'],
                            last_name=data['last_name'],
                            username=data['username'],
                            global_content=global_content,
                            current_user=current_user, 
                            active_clipcards_count=data['active_clipcards_count'],
                            inactive_clipcards_count=data['inactive_clipcards_count'],
                            time_used_hours=data['time_used_hours'],
                            time_used_minutes=data['time_used_minutes'],
                            remaining_hours=data['remaining_hours'],
                            remaining_minutes=data['remaining_minutes'])
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
                            global_content=global_content, 
                            selling_points=selling_points, 
                            social_media=social_media, 
                            current_user=current_user, 
                            )
    except Exception as e:
        logger.error("Error loading template '%s': %s", template_name, e)
        return f"Error loading template {template_name}: {e}"
    finally:
        logger.info("Template request for '%s' completed.", template_name)

 # type: ignore