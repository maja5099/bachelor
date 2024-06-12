##############################
#   IMPORTS
#   Library imports
from bottle import template, get, post, request, delete, template, HTTPResponse
import time
import uuid
import logging

#   Local application imports
from common.colored_logging import setup_logger
import common.content as content
from common.get_current_user import *
from common.find_template import *
from common.time_formatting import *
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
#   DATABASE INITIALIZATION
db = master.db()


##############################
#   LOAD PROFILE DATA
#   Fetching information to be included in the admin/customer profile
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

        # Retrieve task details for the current user, ordered by creation date
        tasks_query = """
            SELECT task_title, task_description, time_spent, created_at
            FROM tasks
            WHERE customer_id = ?
            ORDER BY created_at DESC
        """

        # Fetch tasks using the current user's ID
        tasks = db.execute(tasks_query, (user['user_id'],)).fetchall()

        # Task details
        formatted_tasks = [{
            'task_title': task['task_title'],
            'task_description': task['task_description'],
            'formatted_time_spent': format_time_spent(task['time_spent']),
            'formatted_created_at': format_created_at(task['created_at'])
        } for task in tasks]

        # Return a dictionary of all relevant information
        return {
            'user': user,
            'first_name': user['first_name'],
            'last_name': user['last_name'],
            'username': user['username'],
            'time_used_hours': time_used_hours,
            'time_used_minutes': time_used_minutes,
            'remaining_hours': remaining_hours,
            'remaining_minutes': remaining_minutes,
            'tasks': formatted_tasks
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
#   CUSTOMER CLIPCARD
@get('/profile/profile_customer_clipcard')
def clipcards():

    page_name = "clipcards"

    try:
        # Check if response is HTTP response
        data = load_profile_data()
        if isinstance(data, HTTPResponse):
            return data

        if not data:
            logger.error("Failed to load profile data.")
            return "Error loading data."

        # Retrieve current user details
        current_user = get_current_user()
        if current_user:
            # Establish database connection
            db = master.db()
            logger.debug(f"Database connection opened for {page_name}")

            # Retrieve current user and fetch clipcard ID if available
            user_id = current_user['user_id']
            clipcard_id = db.execute("SELECT clipcard_id FROM payments WHERE user_id = ? LIMIT 1", (user_id,)).fetchone()

            # Default to no active clipcard
            current_user['has_active_clipcard'] = False

            # If active clipcard
            if clipcard_id:
                clipcard_id_value = clipcard_id['clipcard_id']
                print("Clipcard ID:", clipcard_id_value)

                # Prepare the query to check for active clipcards
                has_active_clipcard_query = """
                SELECT COUNT(*) AS active_clipcards
                FROM clipcards
                WHERE clipcard_id IN (
                    SELECT clipcard_id
                    FROM payments
                    WHERE user_id = ?)
                AND is_active = 1
                """
                # Execute the query and fetch the result
                has_active_clipcard_result = db.execute(has_active_clipcard_query, (user_id,)).fetchone()

                # If the count over 0, then user has active clipcard
                if has_active_clipcard_result and has_active_clipcard_result['active_clipcards'] > 0:
                    current_user['has_active_clipcard'] = True

        # Get clipcard types and prices
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_title, clipcard_price FROM card_types")
        clipcards = cursor.fetchall()
        cursor.close()

        # Determine and load template
        template_path = find_template('profile_customer_clipcard', template_dirs)
        if template_path is None:
            logger.error("Clipcard template not found.")
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(relative_path,
                        global_content=global_content,
                        profile_content=profile_content,
                        services_and_prices_content=services_and_prices_content,
                        clipcards=clipcards,
                        current_user=current_user,
                        first_name=data['first_name'],
                        last_name=data['last_name'],
                        username=data['username'],
                        time_used_hours=data['time_used_hours'],
                        time_used_minutes=data['time_used_minutes'],
                        remaining_hours=data['remaining_hours'],
                        remaining_minutes=data['remaining_minutes'],
                        tasks=data['tasks']
                        )

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {page_name}: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {page_name}")


##############################
#   BUY CLIPCARD
@get('/buy_clipcard/<clipcard_type>/<clipcard_price>')
def buy_clipcard(clipcard_type, clipcard_price):

    page_name = "buy_clipcard"

    # Show template
    logger.success(f"Succesfully showing template for {page_name}")
    return template('buy_clipcard.html',
                    global_content=global_content,
                    profile_content=profile_content,
                    clipcard_type=clipcard_type,
                    clipcard_price=clipcard_price
                    )


##############################
#   ADMIN CLIPCARDS
@get('/profile/profile_admin_clipcard')
def admin_clipcards_get():

    page_name = "profile_admin_clipcard"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Load correct template
        template_path = find_template('profile_admin_clipcard', template_dirs)  # Find the required template
        if template_path is None:
            logger.error(f"Template '{page_name}' not found.")
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')  # Normalize the template path

        # Retrieve information about active clipcards
        cursor = db.cursor()
        cursor.execute("""
            SELECT clipcards.clipcard_id, clipcards.remaining_time, clipcards.time_used, clipcards.created_at,
                   users.user_id, users.first_name, users.last_name, users.username, users.email, users.phone,
                   customers.website_name, customers.website_url, card_types.clipcard_type_title
            FROM clipcards
            JOIN payments ON clipcards.clipcard_id = payments.clipcard_id
            JOIN users ON payments.user_id = users.user_id
            JOIN customers ON users.user_id = customers.customer_id
            JOIN card_types ON clipcards.clipcard_type_id = card_types.clipcard_type_id
            WHERE clipcards.is_active = 1;
        """)
        active_clipcards = cursor.fetchall()
        cursor.close()

        if not active_clipcards:
            logger.info("No active clipcards found.")
            return template(relative_path, active_clipcards=[], active_customers=[])

        # Format time in each clipcard
        formatted_clipcards = []
        active_customers = []
        for clipcard in active_clipcards:
            try:
                # Convert time used and remaining time (from minutes to hours and minutes)
                clipcard['time_used_hours'], clipcard['time_used_minutes'] = minutes_to_hours_minutes(clipcard['time_used'])
                clipcard['remaining_time_hours'], clipcard['remaining_time_minutes'] = minutes_to_hours_minutes(clipcard['remaining_time'])
                clipcard['formatted_created_at'] = format_created_at(clipcard['created_at'])

                # Format the text for time used
                if clipcard['time_used_minutes'] > 0:
                    clipcard['time_used_text'] = f"{clipcard['time_used_hours']} timer og {clipcard['time_used_minutes']} minutter"
                else:
                    clipcard['time_used_text'] = f"{clipcard['time_used_hours']} timer"

                # Format the text for remaining time
                if clipcard['remaining_time_minutes'] > 0:
                    clipcard['remaining_time_text'] = f"{clipcard['remaining_time_hours']} timer og {clipcard['remaining_time_minutes']} minutter"
                else:
                    clipcard['remaining_time_text'] = f"{clipcard['remaining_time_hours']} timer"

                # Add the formatted clipcard to the list of formatted clipcards
                formatted_clipcards.append(clipcard)

                # Collect user information conneced with clipcard
                active_customers.append({
                    'user_id': clipcard['user_id'],
                    'first_name': clipcard['first_name'],
                    'last_name': clipcard['last_name'],
                    'clipcard_id': clipcard['clipcard_id']
                })

                logger.success(f"Processed clipcard {clipcard['clipcard_id']} for user {clipcard['user_id']}")

            except Exception as e:
                logger.error(f"Error processing clipcard {clipcard['clipcard_id']}: {e}")

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(
            relative_path,
            global_content=global_content,
            profile_content=profile_content,
            formatted_clipcards=formatted_clipcards,
            active_clipcards=active_clipcards,
            active_customers=active_customers
        )

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {page_name}: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {page_name}")


##############################
#   ADMIN HOUR REGISTRATION
@get('/profile/profile_admin_hour_registration')
def admin_clipcards_get():

    page_name = "profile_admin_hour_registration"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Load correct template
        template_path = find_template('profile_admin_hour_registration', template_dirs)  # Locate the template
        if template_path is None:
            logger.error("Hour registration template not found")
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')  # Normalize template path

        # Fetch active clipcards and user information
        cursor = db.cursor()
        cursor.execute("""
            SELECT clipcards.clipcard_id, clipcards.remaining_time, clipcards.time_used, clipcards.created_at,
                   users.user_id, users.first_name, users.last_name, users.username, users.email, users.phone,
                   customers.website_name, customers.website_url, card_types.clipcard_type_title
            FROM clipcards
            JOIN payments ON clipcards.clipcard_id = payments.clipcard_id
            JOIN users ON payments.user_id = users.user_id
            JOIN customers ON users.user_id = customers.customer_id
            JOIN card_types ON clipcards.clipcard_type_id = card_types.clipcard_type_id
            WHERE clipcards.is_active = 1;
        """)
        active_clipcards = cursor.fetchall()
        cursor.close()

        if not active_clipcards:
            logger.info("No active clipcards found")
            return template(relative_path, active_clipcards=[], active_customers=[])

        # List of dictionaries for each active customer and clipcard ID
        active_customers = [{
            'user_id': row['user_id'],
            'first_name': row['first_name'],
            'last_name': row['last_name'],
            'clipcard_id': row['clipcard_id']
        } for row in active_clipcards]

        # Format time data on each clipcard
        formatted_clipcards = []
        for clipcard in active_clipcards:
            clipcard['time_used_hours'], clipcard['time_used_minutes'] = minutes_to_hours_minutes(clipcard['time_used'])
            clipcard['remaining_time_hours'], clipcard['remaining_time_minutes'] = minutes_to_hours_minutes(clipcard['remaining_time'])
            clipcard['formatted_time_text'] = f"{clipcard['time_used_hours']} hours and {clipcard['time_used_minutes']} minutes" if clipcard['time_used_minutes'] else f"{clipcard['time_used_hours']} hours"
            clipcard['formatted_remaining_time_text'] = f"{clipcard['remaining_time_hours']} hours and {clipcard['remaining_time_minutes']} minutes" if clipcard['remaining_time_minutes'] else f"{clipcard['remaining_time_hours']} hours"
            formatted_clipcards.append(clipcard)

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(relative_path,
                        global_content=global_content,
                        profile_content=profile_content,
                        active_clipcards=formatted_clipcards,
                        active_customers=active_customers
                        )

    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {page_name}: {e}")
        response.status = 500
        return {"error": "Internal Server Error"}

    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {page_name}")


##############################
#   DELETE CLIPCARD
@delete('/delete_clipcard/<clipcard_id>')
def delete_clipcard(clipcard_id):

    function_name = "delete_clipcard"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        cursor = db.cursor()

        # Check if the clipcard exists
        cursor.execute("SELECT * FROM clipcards WHERE clipcard_id = ?", (clipcard_id,))
        existing_clipcard = cursor.fetchone()

        # Error if no clipcard
        if existing_clipcard is None:
            logger.error(f"No clipcard found with ID: {clipcard_id}")
            return {"info": f"The clip card with id {clipcard_id} does not exist."}

        # Info if already has been deleted
        if existing_clipcard["is_active"] == "0":
            logger.info(f"Clipcard {clipcard_id} has already been deleted.")
            return {"info": f"The clip card with id {clipcard_id} has already been deleted."}

        # Update clipcard as deleted
        updated_at = int(time.time())
        deleted_at = int(time.time())
        cursor.execute("""
            UPDATE clipcards
            SET updated_at = ?, deleted_at = ?, is_active = 0
            WHERE clipcard_id = ?
        """, (updated_at, deleted_at, clipcard_id))

        # Commit changes to the database
        db.commit()
        logger.success(f"{function_name} successful, clipcard {clipcard_id} deleted successfully")
        return {"message": f"{function_name} successful"}

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
#   SUBMIT TASK
@post('/submit_task')
def submit_task():

    function_name = "signup"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        cursor = db.cursor()

        # Retrieve form data
        user_id = request.forms.get('customer')
        task_title = request.forms.get('title')
        task_description = request.forms.get('description')
        hours = int(request.forms.get('hours', '0') or '0')
        minutes = int(request.forms.get('minutes', '0') or '0')

        # Calculate total time spent in minutes
        time_spent = hours * 60 + minutes
        created_at = int(time.time())

        logger.debug(f"Form data received: user_id={user_id}, task_title={task_title}, hours={hours}, minutes={minutes}")

        # Check for an active clipcard associated with the user
        result = cursor.execute("""
            SELECT payments.clipcard_id
            FROM payments
            JOIN clipcards ON payments.clipcard_id = clipcards.clipcard_id
            WHERE payments.user_id = ? AND clipcards.is_active = 1
        """, (user_id,)).fetchone()

        if result is None:
            logger.warning("No active clipcard found for the user")
            return {"info": "No active clipcard found for the provided user_id."}

        # Insert new task into the database
        task_id = str(uuid.uuid4().hex)
        cursor.execute("""
            INSERT INTO tasks (task_id, clipcard_id, customer_id, task_title, task_description, created_at, time_spent)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (task_id, result["clipcard_id"], user_id, task_title, task_description, created_at, time_spent))

        # Commit changes to the database
        db.commit()

        # Update clipcard usage
        time_data = cursor.execute("""
            SELECT time_used, remaining_time
            FROM clipcards
            WHERE clipcard_id = ?
        """, (result["clipcard_id"],)).fetchone()

        # Update if time data exists
        if time_data:
            time_used_minutes = time_data["time_used"] + time_spent
            remaining_time_minutes = time_data["remaining_time"] - time_spent
            cursor.execute("""
                UPDATE clipcards
                SET time_used = ?, remaining_time = ?
                WHERE clipcard_id = ?
            """, (time_used_minutes, remaining_time_minutes, result["clipcard_id"]))

            # Commit changes to the database
            db.commit()

        logger.success(f"{function_name} successful, task successfully submitted")
        return {"info": "Opgaven er registreret!"}

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
