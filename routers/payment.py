##############################
#   IMPORTS
#   Library imports
from bottle import post, request, template
import uuid
import time
import logging
import os
from common.get_current_user import get_current_user

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


global_content=content.global_content


##############################
#   PROCESS PAYMENT
@post('/process_payment')
def process_payment():

    function_name = "process_payment"

    try:
        current_user = get_current_user()
        if not current_user:
            logger.error("User information not found in session.")
            raise Exception('User information not found in session.')

        user_id = current_user['user_id']
        if not user_id:
            logger.error("User ID not found for the current session.")
            raise Exception('User ID not found.')

        # Payment details retrieval
        clipcard_price = request.forms.get('clipcard_price')
        amount_paid = clipcard_price 
        payment_id = str(uuid.uuid4())
        clipcard_id = str(uuid.uuid4())
        created_at = int(time.time())
        updated_at = int(time.time())
        is_active = 1
        clipcard_type_title = request.forms.get('clipcard_type')
        time_used = 0

        # Database operations
        db = master.db()
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_id, clipcard_type_time FROM card_types WHERE clipcard_type_title = ?", (clipcard_type_title,))
        row = cursor.fetchone()

        if not row:
            logger.error("Clipcard type not found.")
            raise Exception('Clipcard type not found')

        clipcard_type_id = row['clipcard_type_id'] 
        remaining_time = row['clipcard_type_time']  

        # Insert payment and clipcard data
        cursor.execute("INSERT INTO payments (payment_id, user_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
                       (payment_id, user_id, clipcard_id, amount_paid, created_at))
        
        cursor.execute("INSERT INTO clipcards (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active)) 
        
        db.commit()
        cursor.close()

        logger.success("Payment processed successfully, redirecting to confirmation.")
        
        return template("confirmation", title="Confirmation", global_content=global_content, clipcard_type_title=clipcard_type_title, payment_id=payment_id, amount_paid=amount_paid, created_at=created_at)
    
    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for {function_name}: {e}")
        raise
    
    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for {function_name}")