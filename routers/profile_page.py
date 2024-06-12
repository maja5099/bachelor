##############################
#   IMPORTS
#   Library imports
from bottle import get, template, route, HTTPResponse
import logging

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import *
from common.find_template import *
from common.time_formatting import *
import common.content as content
import routers.messages as messages
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
#   Content from content.py
try:
    global_content = content.global_content
    services_and_prices_content = content.services_and_prices_content
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error("Error importing content: %s", e)
finally:
    logger.info("Content import process completed.")


##############################
#   LOAD PROFILE DATA
#   Fetching information to be included in customer clipcards / timeregistration
def load_profile_data():

    function_name = "load_profile_data"

    try:
        # Retrieve current user details
        current_user = get_current_user()

        # Redirect if not logged in
        if not current_user:
            logger.info("No current user found, redirecting to login.")
            return HTTPResponse(status=303, headers={"Location": "/"})

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        user = current_user

        # Retrieve active clipcard ID for the current user
        payment_query = """
            SELECT payments.clipcard_id
            FROM payments
            WHERE payments.user_id = ? AND payments.clipcard_id IN (SELECT clipcard_id FROM clipcards WHERE is_active = 1)
            LIMIT 1
        """

        # Fetch the result
        payment = db.execute(payment_query, (user['user_id'],)).fetchone()

        # Initialize variables for time
        time_used_hours = time_used_minutes = remaining_hours = remaining_minutes = 0

        # If a valid payment and clipcard are found, retrieve detailed clipcard data
        if payment and payment['clipcard_id']:
            clipcard_data = db.execute("""
                SELECT time_used, remaining_time
                FROM clipcards
                WHERE clipcard_id = ? AND is_active = 1
            """, (payment['clipcard_id'],)).fetchone()

            # If clipcard data is found, convert time
            if clipcard_data:
                time_used_hours, time_used_minutes = minutes_to_hours_minutes(clipcard_data['time_used'])
                remaining_hours, remaining_minutes = minutes_to_hours_minutes(clipcard_data['remaining_time'])
            else:
                logger.info("Active clipcard data not found for user.")
        else:
            logger.info("No active payment found for user.")

        # Count active and inactive clipcards
        active_clipcards_count = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 1").fetchone()['count']
        inactive_clipcards_count = db.execute("SELECT COUNT(*) AS count FROM clipcards WHERE is_active = 0").fetchone()['count']

        # Return a dictionary of all relevant information
        return {
            'user': user,
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'username': user['username'],
            'active_clipcards_count': active_clipcards_count,
            'inactive_clipcards_count': inactive_clipcards_count,
            'time_used_hours': time_used_hours,
            'time_used_minutes': time_used_minutes,
            'remaining_hours': remaining_hours,
            'remaining_minutes': remaining_minutes,
        }

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


##############################
#   PROFILE
@get("/profile")
def profile():

    page_name = "profile"

    try:
        # Check if response is HTTP response
        data = load_profile_data()
        if isinstance(data, HTTPResponse):
            return data

        # Retrieve current user details
        current_user = get_current_user()

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template('profile', title="Din profil",
                        current_user=current_user,
                        profile_content=profile_content,
                        global_content=global_content,
                        services_and_prices_content=services_and_prices_content,
                        user=data['user'],
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        active_clipcards_count=data['active_clipcards_count'],
                        inactive_clipcards_count=data['inactive_clipcards_count'],
                        time_used_hours=data['time_used_hours'],
                        time_used_minutes=data['time_used_minutes'],
                        remaining_hours=data['remaining_hours'],
                        remaining_minutes=data['remaining_minutes'])

    except Exception as e:
        logger.error(f"Error during request for /{page_name}: {e}")
        raise

    finally:
        logger.info(f"Completed request for /{page_name}")


##############################
#   PROFILE TEMPLATE
@route('/profile/<template_name>')
def profile_template(template_name):

    function_name = "profile_template"

    try:
        # Check if response is HTTP response
        data = load_profile_data()
        if isinstance(data, HTTPResponse):
            return data

        # Retrieve current user details
        current_user = get_current_user()

        # Determine and load template
        template_path = find_template(template_name, template_dirs)
        if template_path is None:
            logger.error(f"Template '{template_name}' not found.")
            return "Template not found."

        # Handle cases for 'profile_overview' that require detailed user information
        if template_name == "profile_overview":
            if current_user:
                db = master.db()
                clipcard_info = db.execute("SELECT clipcard_id FROM payments WHERE user_id = ? LIMIT 1", (current_user['user_id'],)).fetchone()
                if clipcard_info and clipcard_info['clipcard_id']:
                    has_active_clipcard = db.execute("""
                        SELECT COUNT(*) AS active_clipcards
                        FROM clipcards
                        WHERE clipcard_id = ? AND is_active = 1
                    """, (clipcard_info['clipcard_id'],)).fetchone()['active_clipcards'] > 0
                    current_user['has_active_clipcard'] = has_active_clipcard

            # Adjust relative path for rendering
            relative_path = template_path.replace('views/', '').replace('.tpl', '')
            return template(relative_path,
                            profile_content=profile_content,
                            current_user=current_user,
                            global_content=global_content,
                            services_and_prices_content=services_and_prices_content,
                            user=data['user'],
                            first_name=data['first_name'],
                            last_name=data['last_name'],
                            username=data['username'],
                            active_clipcards_count=data['active_clipcards_count'],
                            inactive_clipcards_count=data['inactive_clipcards_count'],
                            time_used_hours=data['time_used_hours'],
                            time_used_minutes=data['time_used_minutes'],
                            remaining_hours=data['remaining_hours'],
                            remaining_minutes=data['remaining_minutes']
                            )        
        # General template rendering for other templates
        else:
            relative_path = template_path.replace('views/', '').replace('.tpl', '')
            logger.success(f"Succesfully showing template for {function_name}")
            return template(relative_path,
                            title="Din profil",
                            profile_content=profile_content,
                            save_file=messages.save_file,
                            get_current_user=messages.get_current_user,
                            send_message=messages.send_message,
                            messages_get=messages.messages_get,
                            admin_messages_get=messages.admin_messages_get,
                            delete_message=messages.delete_message,
                            current_user=current_user,
                            global_content=global_content,
                            services_and_prices_content=services_and_prices_content,
                            user=data['user'],
                            first_name=data['first_name'],
                            last_name=data['last_name'],
                            username=data['username'],
                            )

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
