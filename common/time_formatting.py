##############################
#   IMPORTS
#   Library imports
from datetime import datetime
from math import floor
import logging

#   Local application imports
from common.colored_logging import setup_logger


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
#   TIME FORMATTING
#   Format minutes to hours and minutes
def minutes_to_hours_minutes(minutes):

    function_name = "minutes_to_hours_minutes"
    
    try:
        # Calculate hours from total minutes, and determine remaining minutes
        hours = floor(minutes / 60)
        remaining_minutes = minutes % 60

        logger.success(f"Executed {function_name} successfully")
        return hours, remaining_minutes
    
    except Exception as e:
        logger.error(f"Error during {function_name}: {e}")
        return None
    
    finally:
        logger.info(f"Completed {function_name}")


#   Format time spent
def format_time_spent(minutes):

    function_name = "format_time_spent"

    try:
        # Check if total minutes are less than or equal to 60
        if minutes <= 60:
            logger.success(f"Executed {function_name} successfully")
            return f"{minutes} minutter"
        
        # Calculate hours and remaining minutes if total minutes is over 60
        else:
            hours = minutes // 60
            remaining_minutes = minutes % 60

            logger.success(f"Executed {function_name} successfully")
            return f"{hours} timer og {remaining_minutes} minutter"
        
    except Exception as e:
        logger.error(f"Error during {function_name}: {e}")
        return "Fejl i format"
    
    finally:
        logger.info(f"Completed {function_name}")


#   Format timestamp
def format_created_at(timestamp):

    function_name = "format_time_spent"

    try:
        # Check if timestamp is a string and convert to integer
        if isinstance(timestamp, str):
            try:
                timestamp = int(timestamp)
            except ValueError:
                logger.error("Timestamp can not be converted to an integer.")
                return None
            
        # Convert timestamp to datetime, and format it into a readable date
        created_at_dt = datetime.fromtimestamp(timestamp)
        formatted_created_at = created_at_dt.strftime('%d-%m-%Y %H:%M')

        logger.success(f"Executed {function_name} successfully")
        return formatted_created_at
    
    except Exception as e:
        logger.error(f"Error during {function_name}: {e}")
        return None
    
    finally:
        logger.info(f"Completed {function_name}")