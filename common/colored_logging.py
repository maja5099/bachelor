# INSPIRED BY: https://gist.github.com/hit9/5635505

##############################
#   IMPORTS
#   Library imports
import logging


##############################
#   COLORED LOGGING
class ColoredFormatter(logging.Formatter):
    # Define colors for log levels (ANSI)
    colors = {
        'INFO': 36, 'WARNING': 33, 'ERROR': 31,
        'CRITICAL': 41, 'DEBUG': 100, 'SUCCESS': 32
    }
    def format(self, record):
        # Retrieve colors code for the log levels (default white)
        color_code = self.colors.get(record.levelname, 37)
        
        # Format the log message with level name and color
        return f"\033[{color_code}m{record.levelname}\033[0m: {record.getMessage()}"

def setup_logger(name, level=logging.INFO):
    # Set up logger to show logs with the colors
    logger = logging.getLogger(name)
    handler = logging.StreamHandler()
    handler.setFormatter(ColoredFormatter())
    logger.addHandler(handler)
    logger.setLevel(level)

    # Add a custom log level 'SUCCESS' (not in Python's logging)
    logging.SUCCESS = 25
    logging.addLevelName(logging.SUCCESS, 'SUCCESS')

    # Custom method to the success level
    logger.success = lambda message, *args: logger._log(logging.SUCCESS, message, args)
    return logger