##############################
#   IMPORTS
#   Library imports
from bottle import default_app, route, get, request, error, run, template, static_file, TEMPLATE_PATH
import logging
import json
import git
import os


#   Local application imports
from routers.messages import UPLOADS_FOLDER
from colored_logging import setup_logger
import content
import master

#   Initialising app at module level
application = default_app()


##############################
#   COLERED LOGGING
logger = setup_logger(__name__, level=logging.INFO)
logger.setLevel(logging.INFO)


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
        logger.error("Error updating git repository: %s", e)
    finally:
        logger.info("Git update process completed.")


##############################
#   ERROR HANDLING
def handle_error(error_code, error):
    try:
        if error:
            logger.error(f"Handled {error_code} succesfully with following error details: {error}")
            return template('error', 
                            title=error_content['title'], 
                            error=error, 
                            error_image=error_content['image'], 
                            button_link=error_content['button_link'], 
                            button_text=error_content['button_text'], 
                            error_title=error_content[str(error_code)]['error_title'], 
                            error_message=error_content[str(error_code)]['error_message'])
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
    logger.error("Error setting icons path: %s", e)
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
    import routers.profile
    import routers.services_and_prices
    import routers.signup
    logger.success("Routers imported successfully.")
except Exception as e:
    logger.error("Error importing routers: %s", e)
finally:
    logger.info("Router import process completed.")


##############################
#   CONTENT (FROM CONTENT.PY)
try:
    error_content = content.error_content
    footer_info = content.footer_info
    form_inputs = content.form_inputs
    header_nav_items = content.header_nav_items
    section_landingpage_hero_content = content.section_landingpage_hero_content
    section_profile_admin = content.section_profile_admin
    section_profile_customer = content.section_profile_customer
    section_testimonial_content = content.section_testimonial_content
    selling_points = content.selling_points
    social_media = content.social_media
    ui_icons = content.ui_icons
    unid_logo = content.unid_logo
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error("Error importing content: %s", e)
finally:
    logger.info("Content import process completed.")


##############################
#   INDEX
@route("/")
def index():
    # Retrieve the user cookie
    user_cookie = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
    logger.info("Found user cookie: %s", user_cookie)

    # Variables set to none to ensure they have a defined value even if user is not found (prevents error)
    user = None
    username = first_name = last_name = None

    # If cookie is found / user is logged in
    if user_cookie:
        try:
            # Check if user_cookie is a dictionary or a string
            if isinstance(user_cookie, str):
                user_data = json.loads(user_cookie)
                logger.info("User data extracted: %s", user_data)
            else:
                user_data = user_cookie
                logger.info("User data extracted: %s", user_data)
            
            # Database connection
            db = master.db()
            user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (user_data['username'],)).fetchone()
            
            # User is found in the database
            if user:
                username = user['username']
                first_name = user['first_name']
                last_name = user['last_name']
                logger.success("User found in database: %s", username)
            
            # User is not found in the database
            else:
                logger.info("User not found in database: %s", user_data['username'])
        
        # Error decoding cookie
        except Exception as e:
            logger.error("Error decoding user_cookie, perhaps user is not logged in yet. Error: %s", e)

        # Always executed   
        finally:
            logger.info("Completed user authentication process.")
    
    # If cookie is not found / user is not logged in
    else:
        logger.info("No user cookie found.")

    return template('index', 
                    title="UNID Studio", 
                    error_content=error_content, 
                    first_name=first_name, 
                    footer_info=footer_info, 
                    form_inputs=form_inputs, 
                    header_nav_items=header_nav_items, 
                    last_name=last_name, 
                    section_landingpage_hero_content=section_landingpage_hero_content, 
                    section_profile_admin=section_profile_admin, 
                    section_profile_customer=section_profile_customer, 
                    section_testimonial_content=section_testimonial_content, 
                    selling_points=selling_points, 
                    social_media=social_media, 
                    testimonials=section_testimonial_content['testimonials'], 
                    ui_icons=ui_icons, 
                    unid_logo=unid_logo, 
                    user=user, 
                    username=username
                    )


##############################
#   LOCAL HOST
if __name__ == "__main__":
    try:
        logger.success("Running local server")
        run(host="127.0.0.1", port=2000, debug=True, reloader=True)
    except Exception as e:
        logger.error(f"Error running local server: {e}")
    finally:
        logger.info("Local host setup completed.")