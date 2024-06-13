##############################
#   IMPORTS
#   Library imports
import logging
import os

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
#   FIND TEMPLATE
# Directory list where templates are expected to be found
template_dirs = ['components', 'elements', 'sections', 'utilities', 'profile', 'admin', 'customers', 'components/profile/admin', 'components/profile/customer']


def find_template(template_name, directories):

    function_name = "get_current_user"
    base_path = 'views'

    try:
        # Go through directories to find the specified template
        for directory in directories:
            path = os.path.join(base_path, directory)
            print(f"Checking directory: {path}")

            # If the template is found
            for root, dirs, files in os.walk(path):
                print(f"Visited {root}")
                if f'{template_name}.tpl' in files:
                    template_path = os.path.join(root, template_name + '.tpl')
                    print(f"Executed {function_name} successfully and found template at: {template_path}")
                    return template_path

        # If the template is not found in any of the specified directories
        print("Template not found")
        return None

    except Exception as e:
        logger.error(f"An error occurred during {function_name} while searching for the template: {e}")
        return None

    finally:
        logger.info(f"Completed {function_name} for {template_name}")
