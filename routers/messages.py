##############################
#   IMPORTS
#   Library imports
from bottle import post, get, request, response, template, delete
import logging
import os
import uuid
import time

#   Local application imports
from common.colored_logging import setup_logger
from common.get_current_user import get_current_user
from common.find_template import *
from common.time_formatting import *
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
    global_content = content.global_content
    # Content for this page
    profile_content = content.profile_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


###############################
#   DIR CONFIGS
# Application base directory
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  

# Uploaded files path
UPLOADS_FOLDER = os.path.join(ROOT_DIR, "uploads") 


###############################
#   SAVE FILE FUNCTION
def save_file(upload=None):

    function_name = "save_file"

    try:
        if upload and upload.filename:
            allowed_extensions = {'png', 'jpg', 'jpeg'}
            file_extension = upload.filename.rsplit('.', 1)[1].lower()

            # Check if the file extension is in the allowed formats
            if file_extension in allowed_extensions:
                # Generate a unique filename
                file_name = str(uuid.uuid4()) + '.' + file_extension
                file_path = os.path.join(UPLOADS_FOLDER, file_name)

                # Open the new file path
                with open(file_path, "wb") as open_file:
                    open_file.write(upload.file.read())
                logger.info(f"File saved successfully: {file_name}")
                return "/uploads/" + file_name
            
            else:
                logger.error("File extension not allowed.")

        return None
    
    except Exception as e:
        logger.error(f"Error during {function_name}: {e}")
        return None
    
    finally:
        logger.info(f"Completed {function_name}.")
 

##############################
#   SEND MESSAGE
#   Endpoint to send a message
@post('/send_message')
def send_message():

    function_name = "send_message"

    try:
        # Retrieve data from the form
        message_subject = request.forms.get('subject')
        message_text = request.forms.get('message')
        message_file = request.files.get('file')

        # Check for required fields
        if not message_subject or not message_text:
            response.status = 400
            return {"info": "Emne og beskedtekst er påkrævet"}

        # Save attached file and construct a file path
        file_path = save_file(message_file) or ""

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")
        cursor = db.cursor()

        # Generate a unique identifier for the new message
        message_id = str(uuid.uuid4().hex)

        # Retrieve current user details
        current_user = get_current_user()
        if not current_user:
            response.status = 401
            return {"info": "User not logged in"}
        user_id = current_user['user_id']

        #  Prepare timestamp for the the new message
        created_at = int(time.time())
        deleted_at = ""
        
        # Insert user data into messages table
        cursor.execute("""
            INSERT INTO messages (message_id, user_id, message_subject, message_text, message_file, created_at, deleted_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (message_id, user_id, message_subject, message_text, file_path, created_at, deleted_at))

        # Commit changes to the database
        db.commit()
        logger.success(f"{function_name} successful")
        return {"info": "Beskeden er blevet sendt!"}

    except ValueError as ve:
        logger.error(f"ValueError during {function_name}: {ve}")
        response.status = 400
        return {"info": str(ve)}
    
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
#   MESSAGES
@get("/messages")
def messages_get():

    page_name = "messages_get"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Find the template and remove path and file extension
        template_path = find_template('profile_customer_messages', template_dirs)
        if template_path is None:
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(relative_path, 
                        global_content=global_content, 
                        profile_content=profile_content
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
#   ADMIN MESSAGES GET
@get('/profile/profile_admin_messages')
def admin_messages_get():

    page_name = "admin_messages_get"

    try:
        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {page_name}")

        # Set up cursor and execute query to fetch message details
        cursor = db.cursor()
        cursor.execute("""
            SELECT 
                messages.message_id,
                messages.created_at,
                messages.message_subject, 
                messages.message_text, 
                messages.message_file,
                users.first_name, 
                users.last_name, 
                customers.website_name,
                customers.website_url
            FROM messages
            JOIN users ON messages.user_id = users.user_id
            JOIN customers ON messages.user_id = customers.customer_id
            WHERE messages.deleted_at IS ""
            ORDER BY messages.created_at DESC;
        """)

        # Retrieve all messages from the query and print
        messages = cursor.fetchall()
        print(messages)

        # Format the creation date of each message
        formatted_messages = []
        for message in messages:
            message['formatted_created_at'] = format_created_at(message['created_at'])
            formatted_messages.append(message)

        # Find the template and remove path and file extension
        template_path = find_template('profile_admin_messages', template_dirs)
        if template_path is None:
            return "Template not found."
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        # Show template
        logger.success(f"Succesfully showing template for {page_name}")
        return template(relative_path, 
                        messages=messages, 
                        global_content=global_content, 
                        profile_content=profile_content
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
#   DELETE
@delete('/delete_message')
def delete_message():

    function_name = "delete_message"

    try:
        # Retrieve message ID from the form data
        message_id = request.forms.get('message_id')
        if not message_id:
            logger.warning(f"Message ID missing in {function_name}")
            response.status = 400
            return {"info": "Message ID is missing."}

        # Confirm current user is logged in
        current_user = get_current_user()
        if not current_user:
            logger.warning(f"User not logged in during {function_name}")
            response.status = 401
            return {"info": "User not logged in."}

        logger.info(f"Attempting to delete message with ID: {message_id}")

        # Set timestamp
        deleted_at = int(time.time())

        # Establish database connection
        db = master.db()
        logger.debug(f"Database connection opened for {function_name}")
        cursor = db.cursor()

        # Set the deleted_at for specified message
        cursor.execute("""
            UPDATE messages 
            SET deleted_at = ?
            WHERE message_id = ? 
        """, (deleted_at, message_id))

        # Commit changes to the database
        db.commit()

        # Check if the message was actually found and updated
        if cursor.rowcount == 0:
            logger.error(f"Message with ID {message_id} not found in {function_name}")
            response.status = 404
            return {"info": "Message not found."}

        # Log successful deletion
        logger.info(f"Message with ID {message_id} deleted successfully")
        return {"info": "Message deleted."}

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