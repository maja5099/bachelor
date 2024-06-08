##############################
#   IMPORTS
#   Library imports
import logging
import os

#   Local application imports
from colored_logging import setup_logger


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
#   FIND TEMPLATE
template_dirs = ['components', 'elements', 'sections', 'utilities', 'profile', 'profile/admin']

def find_template(template_name, directories):
    base_path = 'views'
    for directory in directories:
        path = os.path.join(base_path, directory)
        print(f"Checking directory: {path}")
        for root, dirs, files in os.walk(path):
            print(f"Visited {root}")
            if f'{template_name}.tpl' in files:
                template_path = os.path.join(root, template_name + '.tpl')
                print(f"Found template at: {template_path}")
                return template_path
    print("Template not found")
    return None