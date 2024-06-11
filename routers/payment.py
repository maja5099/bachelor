##############################
#   IMPORTS
#   Library imports
from bottle import post, request, template
import uuid
import time
import logging

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import get_current_user
import common.content as content
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
#   CONTENT VARIABLES
try:
    # Global
    global_content=content.global_content
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   PROCESS PAYMENT
@post('/process_payment')
def process_payment():

    function_name = "process_payment"

    try:
        # Authenticate and identify the current user
        current_user = get_current_user()
        if not current_user:
            logger.error("User information not found in session.")
            raise Exception('User information not found in session.')

        user_id = current_user['user_id']
        if not user_id:
            logger.error("User ID not found for the current session.")
            raise Exception('User ID not found.')

        # Retrieve payment details from the form
        clipcard_price = request.forms.get('clipcard_price')
        amount_paid = clipcard_price 
        payment_id = str(uuid.uuid4())
        clipcard_id = str(uuid.uuid4())
        created_at = int(time.time())
        updated_at = int(time.time())
        is_active = 1
        clipcard_type_title = request.forms.get('clipcard_type')
        time_used = 0

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")

        # Retrieve clipcard type details from database
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_id, clipcard_type_time FROM card_types WHERE clipcard_type_title = ?", (clipcard_type_title,))
        row = cursor.fetchone()

        if not row:
            logger.error("Clipcard type not found.")
            raise Exception('Clipcard type not found')

        clipcard_type_id = row['clipcard_type_id'] 
        remaining_time = row['clipcard_type_time']  

        # Insert payment and clipcard records into the database
        cursor.execute("INSERT INTO payments (payment_id, user_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
                       (payment_id, user_id, clipcard_id, amount_paid, created_at))
        cursor.execute("INSERT INTO clipcards (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active)) 
        
        # Commit changes to the database
        db.commit()
        logger.success(f"{function_name} successful")
        cursor.close()

        # Show template
        logger.success("Payment processed successfully, redirecting to confirmation.")
        return template("confirmation", 
                        title="Confirmation", 
                        # A-Z
                        amount_paid=amount_paid, 
                        clipcard_type_title=clipcard_type_title, 
                        created_at=created_at,
                        global_content=global_content, 
                        payment_id=payment_id, 
                        profile_content=profile_content,
                        )
    
    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during {function_name}: {e}")
        raise
    
    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed {function_name}")