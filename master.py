##############################
#   IMPORTS
#   Library imports
import logging
import sqlite3
import pathlib


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
#   DICT FACTORY
def dict_factory(cursor, row):
    col_names = [col[0] for col in cursor.description]
    return {key: value for key, value in zip(col_names, row)}


##############################
#   DB
def db():
    try:
        db_path = str(pathlib.Path(__file__).parent.resolve()) + "/uniduniverse.db"
        db = sqlite3.connect(db_path)
        db.row_factory = dict_factory
        logger.success("Database connection established successfully.")
        return db
    except Exception as e:
        logger.error(f"Error establishing database connection: {e}")
        raise
    finally:
        logger.info("Database function execution completed.")


