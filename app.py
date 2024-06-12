##############################
#   IMPORTS
#   Library imports
from bottle import default_app, route, get, request, error, run, template, static_file, TEMPLATE_PATH
import logging
import git
import os

#   Local application imports
from routers.messages import UPLOADS_FOLDER
from common.colored_logging import setup_logger
import common.content as content
import master


##############################
#   INITIALIZE APP
application = default_app()


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
#   ROUTERS
try:
    import routers.clipcards
    import routers.contact
    import routers.login
    import routers.logout
    import routers.messages
    import routers.payment
    import routers.portfolio
    import routers.about_us
    import routers.profile_page
    import routers.services_and_prices
    import routers.signup
    logger.success("Routers imported successfully.")
except Exception as e:
    logger.error(f"Error importing routers: {e}")
finally:
    logger.info("Router import process completed.")


##############################
#   GIT AND PYTHONANYWHERE HOOK
def git_update():
    try:
        repo = git.Repo('./bachelor')
        origin = repo.remotes.origin
        repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
        origin.pull()
        logger.success("Git repository updated successfully.")
        return ""
    except Exception as e:
        logger.error(f"Error updating git repository: {e}")
    finally:
        logger.info("Git update process completed.")


##############################
#   ERROR HANDLING
def handle_error(error_code, error):
    try:
        if error:
            logger.error(f"Handled {error_code} succesfully with following error details: {error}")
            return template('error', title="Fejl", error=error, header_text=error_content['header_text'], illustration=error_content['illustration'], illustration_alt=error_content['illustration_alt'], button_link=error_content['button_link'], button_text=error_content['button_text'], error_title_text=error_content[str(error_code)]['error_title_text'], error_message_text=error_content[str(error_code)]['error_message_text'])
        else:
            logger.success(f"Handled {error_code} response successfully with no errors.")
    except Exception as e:
        logger.error(f"Error handling {error_code} response: {e}")
    finally:
        logger.info(f"{error_code} error handling completed.")


@error(404)
def error404(error):
    return handle_error(404, error)

@error(500)
def error500(error):
    return handle_error(500, error)



##############################
#   ICONS
try:
    project_root = os.path.dirname(os.path.abspath(__file__))
    assets_template_path = os.path.join(project_root, 'assets', 'icons')
    TEMPLATE_PATH.append(assets_template_path)
    logger.success("Icons path set successfully.")
except Exception as e:
    logger.error(f"Error setting icons path: {e}")
finally:
    logger.info("Icons path configuration completed.")


##############################
#   STATIC
def serve_static(filepath, root):
    try:
        logger.success(f"Static file {filepath} served successfully.")
        return static_file(filepath, root=root)
    except Exception as e:
        logger.error(f"Error serving static file {filepath}: {e}")
    finally:
        logger.info(f"Static file request completed for {filepath}.")

# CSS file
@get("/app.css")
def css_file_static():
    return serve_static('app.css', '.')

# Assets folder
@route('/assets/<filepath:path>')
def assets_folder_static(filepath):
    return serve_static(filepath, './assets')

# Static folder
@route('/static/<filepath:path>')
def static_folder(filepath):
    return serve_static(filepath, './static')

# Uploads folder
@get('/uploads/<filename:path>')
def uploads_folder_static(filename):
    return serve_static(filename, UPLOADS_FOLDER)


##############################
#   CONTENT (FROM CONTENT.PY)
try:
    # Global
    global_content = content.global_content
    error_content = content.error_content
    # Content for this page
    frontpage_content = content.frontpage_content
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error(f"Error importing content: {e}")
finally:
    logger.info("Content import process completed.")


##############################
#   INDEX
@get("/")
def index():

    page_name = "index"

    try:
        # Securely retrieve user cookie
        user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))

        # Validate cookie, then fetch user details from db
        if user_cookie and isinstance(user_cookie, dict):
            db = master.db()
            username = user_cookie.get('username')
            user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            logger.success(f"Valid user cookie found for /{page_name}, retrieved data from database")
            logger.info(f"Logged in user: {username}")

        # Handle scenarios where no valid cookie is found (e.g., user not logged in)
        else:
            user = username = None
            logger.warning(f"No valid user cookie found for /{page_name}, perhaps user is not logged in yet")

        logger.success(f"Succesfully showing template for {page_name}")
        return template(page_name, title="UNID Studio", global_content=global_content, frontpage_content=frontpage_content, error_content=error_content, user=user, username=username)
    
    except Exception as e:
        if "db" in locals():
            db.rollback()
            logger.info("Database transaction rolled back due to exception")
        logger.error(f"Error during request for /{page_name}: {e}")
        raise
    
    finally:
        if "db" in locals():
            db.close()
            logger.info("Database connection closed")
        logger.info(f"Completed request for /{page_name}")


##############################
#   LOCAL HOST
if __name__ == "__main__":
    try:
        logger.success("Running local server")
        run(host="127.0.0.1", port=2500, debug=True, reloader=True)
    except Exception as e:
        logger.error(f"Error running local server: {e}")
    finally:
        logger.info("Local host setup completed.")