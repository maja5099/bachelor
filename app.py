from bottle import default_app, route, get, request, error, run, template, static_file, TEMPLATE_PATH
import git
import os
import json
import master
import content
import logging
from colored_logging import setup_logger
from routers.messages import UPLOADS_FOLDER


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
@error(404)
def error404(error):
    try:
        logger.success("Handled 404 response succesfully: %s", error)
        return template('error', title=error_content['title'], error=error, error_image=error_content['image'], button_link=error_content['button_link'], button_text=error_content['button_text'], error_title=error_content['404']['error_title'], error_message=error_content['404']['error_message'])
    except Exception as e:
        logger.error("Error handling 404 response: %s", e)
    finally:
        logger.info("404 error handling completed.")

@error(500)
def error500(error):
    try:
        logger.success("Handled 500 response succesfully: %s", error)
        return template('error', title=error_content['title'], error=error, error_image=error_content['image'], button_link=error_content['button_link'], button_text=error_content['button_text'], error_title=error_content['500']['error_title'], error_message=error_content['500']['error_message'])
    except Exception as e:
        logger.error("Error handling 500 response: %s", e)
    finally:
        logger.info("500 error handling completed.")


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
#   CSS file
@get("/app.css")
def css_static():
    try:
        logger.success("Static file CSS served succesfully.")
        return static_file('app.css', root='.')
    except Exception as e:
        logger.error("Error serving static file css: %s", e)
    finally:
        logger.info("Static file css request completed.")

#   Assets folder
@route('/assets/<filepath:path>')
def assets_static(filepath):
    try:
        logger.success("Static folder assets served successfully.")
        return static_file(filepath, root='./assets')
    except Exception as e:
        logger.error("Error serving static folder assets: %s", e)
    finally:
        logger.info("Static folder assets request completed.")

#   Static folder
@route('/static/<filepath:path>')
def static(filepath):
    try:
        logger.success("Static folder served successfully.")
        return static_file(filepath, root='./static')
    except Exception as e:
        logger.error("Error serving static folder: %s", e)
    finally:
        logger.info("Static folder request completed.")

#   Uploads folder
@get('/uploads/<filename:path>')
def uploads_static(filename):
    try:
        logger.success("Static folder uploads served successfully.")
        return static_file(filename, root=UPLOADS_FOLDER)
    except Exception as e:
        logger.error("Error serving static folder uploads: %s", e)
    finally:
        logger.info("Static folder uploads request completed.")


##############################
#   ROUTERS
try:
    import routers.signup
    import routers.login
    import routers.logout
    import routers.profile
    import routers.portfolio
    import routers.contact
    import routers.clipcards
    import routers.payment
    import routers.messages
    logger.success("Routers imported successfully.")
except Exception as e:
    logger.error("Error importing routers: %s", e)
finally:
    logger.info("Router import process completed.")


##############################
#   CONTENT (CONTENT.PY)
try:
    header_nav_items = content.header_nav_items
    footer_info = content.footer_info
    section_landingpage_hero_content = content.section_landingpage_hero_content
    unid_logo = content.unid_logo
    selling_points = content.selling_points
    social_media = content.social_media
    ui_icons = content.ui_icons
    form_inputs = content.form_inputs
    section_profile_admin = content.section_profile_admin
    section_profile_customer = content.section_profile_customer
    section_testimonial_content = content.section_testimonial_content
    error_content = content.error_content
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
        except (json.JSONDecodeError, TypeError) as e:
            logger.error("Error decoding user_cookie, perhaps user is not logged in yet. Error: %s", e)

        # Always executed   
        finally:
            logger.info("Completed user authentication process.")
    
    # If cookie is not found / user is not logged in
    else:
        logger.info("No user cookie found.")

    return template('index', title="UNID Studio", user=user, error_content=error_content, section_testimonial_content=section_testimonial_content, testimonials=section_testimonial_content['testimonials'], section_profile_admin=section_profile_admin, section_profile_customer=section_profile_customer, first_name=first_name, last_name=last_name, username=username, header_nav_items=header_nav_items, footer_info=footer_info, section_landingpage_hero_content=section_landingpage_hero_content, unid_logo=unid_logo, selling_points=selling_points, social_media=social_media, ui_icons=ui_icons, form_inputs=form_inputs)


##############################
#   LOCAL HOST
try:
    import production # type: ignore
    application = default_app()
except ImportError:
    logger.success("Running local server")
    run(host="127.0.0.1", port=2000, debug=True, reloader=True)
except Exception as e:
    logger.error("Error running local server: %s", e)
finally:
    logger.info("Local host setup completed.")
