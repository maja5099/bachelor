# COLERED LOGGING FROM https://gist.github.com/hit9/5635505
import logging
from logging import Formatter, StreamHandler

# ANSI colors to terminal output
class Color:
    """
    Utility to return ANSI colored text.
    """
    colors = {
        'black': 30,
        'red': 31,
        'green': 32,
        'yellow': 33,
        'blue': 34,
        'magenta': 35,
        'cyan': 36,
        'white': 37,
        'bgred': 41,
        'bggrey': 100
    }

    prefix = '\033['
    suffix = '\033[0m'

    @staticmethod
    def colored(text, color='white'):
        clr = Color.colors.get(color, 37)
        return f"{Color.prefix}{clr}m{text}{Color.suffix}"

# Extend Python's Logging Formatter to add ANSI colors based on level
class ColoredFormatter(Formatter):
    def format(self, record):
        message = record.getMessage()
        level_color_map = {
            'INFO': 'cyan',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'bgred',
            'DEBUG': 'bggrey',
            'SUCCESS': 'green'
        }
        clr = level_color_map.get(record.levelname, 'white')
        return f"{Color.colored(record.levelname, clr)}: {message}"

# Configures the logger with the color setup
def setup_logger(name, level=logging.INFO):
    logger = logging.getLogger(name)
    handler = StreamHandler()
    formatter = ColoredFormatter()
    handler.setFormatter(formatter)
    handler.setLevel(level)
    logger.addHandler(handler)

    # Custom level success
    logging.SUCCESS = 25
    logging.addLevelName(logging.SUCCESS, 'SUCCESS')
    setattr(logger, 'success', lambda message, *args: logger._log(logging.SUCCESS, message, args))

    logger.setLevel(level)
    return logger
