# 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
# https://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@github.com/maja5099/bachelor.git

from bottle import default_app, post, route, get, run, template, static_file, TEMPLATE_PATH, request, error
import git
import os
import dbconnection
import content


##############################
#   GIT AND PYTHONANYWHERE HOOK
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./bachelor')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""


##############################
#   ICONS
project_root = os.path.dirname(os.path.abspath(__file__))
assets_template_path = os.path.join(project_root, 'assets', 'icons')
TEMPLATE_PATH.append(assets_template_path)


##############################
#   IMAGES
@get(r"/assets/<filename:re:.*\.(webp|png|jpg|gif|svg)>")
def _(filename):
    return static_file(filename, root="./assets")

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets')


##############################
#   CONTENT (CONTENT.PY)
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

##############################
#   INDEX
@route("/")
def index():
    user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
    if user: 
        db = dbconnection.db()
        username = user['username']
        first_name = user['first_name']
        last_name = user['last_name']
        user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
    else:
        user = None
        username = None
        first_name = None
        last_name = None
    return template('index', title="UNID Studio", user=user, error_content=error_content, section_testimonial_content=section_testimonial_content, testimonials=section_testimonial_content['testimonials'], section_profile_admin=section_profile_admin, section_profile_customer=section_profile_customer, first_name=first_name, last_name=last_name, username=username, header_nav_items=header_nav_items, footer_info=footer_info, section_landingpage_hero_content=section_landingpage_hero_content, unid_logo=unid_logo, selling_points=selling_points, social_media=social_media, ui_icons=ui_icons, form_inputs=form_inputs)


##############################
#   ROUTERS
import routers.signup
import routers.login
import routers.profile
import routers.portfolio
import routers.contact
import routers.clipcards
import routers.payment
import routers.messages

##############################
#   CSS
@get("/app.css")
def _():
    return static_file('app.css', root='.')


##############################
#   ERROR HANDLING
@error(404)
def error404(error):
    return template('error', title=error_content['title'], error=error, error_image=error_content['image'], button_link=error_content['button_link'], button_text=error_content['button_text'], error_title=error_content['404']['error_title'], error_message=error_content['404']['error_message'])

@error(500)
def error500(error):
    return template('error', title=error_content['title'], error=error, error_image=error_content['image'], button_link=error_content['button_link'], button_text=error_content['button_text'], error_title=error_content['500']['error_title'], error_message=error_content['500']['error_message'])


##############################
#   LOCAL HOST
try:
  import production # type: ignore
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=2000, debug=True, reloader=True)