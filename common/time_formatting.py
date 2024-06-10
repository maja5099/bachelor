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