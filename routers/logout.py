from bottle import post, redirect, response, request
import master
import logging
import os
from colored_logging import setup_logger


##############################
#   LOGGING
logger = setup_logger(__name__, level=logging.INFO)
logger.setLevel(logging.INFO)


##############################
#   LOGOUT
@post("/logout")
def logout():
    try:
        # Retrieve the user cookie
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        
        # If cookie is found / user is logged in
        if not user_cookie:
            logger.info("No user cookie found, no user to log out")
            return redirect("/")

        # Database connection
        db = master.db()
        user = db.execute("SELECT * FROM users WHERE username = ?", (user_cookie['username'],)).fetchone()
        
        # User is not found in the database
        if not user:
            logger.error("User not found in database: %s", user_cookie['username'])
            return redirect("/")
        
        # User and cookie found
        username = user['username']
        logger.info("Attempting to log out user: %s", username)
        response.delete_cookie("user")
        logger.success("Successfully logged out user: %s", username)
        return redirect("/")
    
    # Error logging out
    except Exception as e:
        if str(e):
            logger.error("Error logging out user: %s, Error: %s", username, e)
        raise e
    
    # Always executed  
    finally:
        logger.info("Logout process completed.")

