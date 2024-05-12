# 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
# https://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@github.com/maja5099/bachelor.git

from bottle import default_app, post, route, get, run, template, static_file, TEMPLATE_PATH, request
import git
import os
import dbconnection

##############################
#   Git and Pythonanywhere hook
@post('/secret_url_for_git_hook')
def git_update():
  repo = git.Repo('./bachelor')
  origin = repo.remotes.origin
  repo.create_head('main', origin.refs.main).set_tracking_branch(origin.refs.main).checkout()
  origin.pull()
  return ""


##############################
#   Icons
project_root = os.path.dirname(os.path.abspath(__file__))
assets_template_path = os.path.join(project_root, 'assets', 'icons')
TEMPLATE_PATH.append(assets_template_path)


##############################
#   Images
@get(r"/assets/<filename:re:.*\.(webp|png|jpg|gif|svg)>")
def _(filename):
    return static_file(filename, root="./assets")

@route('/assets/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./assets')


##############################
#   Module level variables
unid_logo = {       
    "primary_logo": "primary_logo.svg",
    "logo_alt": "UNID Studio's logo",
}

selling_points = [       
    {"icon": "heart.tpl", "text": "Tilfredshedsgaranti"},
    {"icon": "discount.tpl", "text": "Studierabat"},
    {"icon": "pen.tpl", "text": "Skræddersyet løsning"},
    {"icon": "chat.tpl", "text": "Hurtig kundeservice"}
]

header_nav_items = [
    {"text": "Services & Priser", "link": "/"},
    {"text": "Om UNID Studio", "link": "/"},
    {"text": "Portfolio", "link": "/"},
    {"text": "Cases", "link": "/"},
    {"text": "Kontakt", "link": "/"},
]

footer_info = [
    "UNID Studio © 2023",
    "All rights reserved",
    "CVR nr. 43924451",
]

social_media = {       
    "instagram": {"icon": "instagram.tpl", "link": "https://www.instagram.com/unid.studio/"},
    "linkedin": {"icon": "linkedin.tpl", "link": "https://www.linkedin.com/company/unid-studio/"},
}

section_landingpage_hero_content = {       
    "header_text": "Unikke & skræddersyede løsninger",
    "subheader_text": "Vi bestræber os på, at lave unikke og kvalitets løsninger som opfylder hver enkel kundes behov.",
    "button_text": "Kontakt os",
    "image": "digital_design.svg",
}

ui_icons = {       
    "user_icon": "user.tpl", 
    "burger_icon": "burger.tpl"
}

form_inputs = {
    "username": {
        "label_for": "username",
        "text": "Brugernavn", 
        "icon": "user_circle.tpl", 
        "type": "text",
        "name": "username",
        "inputmode":"text",
        "placeholder": "LoremIpsum",
        "form_info": "",
    },
    "password": {
        "label_for": "pwd",
        "text": "Adgangskode", 
        "icon": "lock.tpl", 
        "type": "password",
        "name": "pwd",
        "inputmode":"text",
        "placeholder": "••••••••",
        "form_info": "Use at least 8 characters, one uppercase, one lowercase and one number.",
    },
    "fname": {
        "label_for": "fname",
        "text": "Fornavn", 
        "icon": "user_name_semi.tpl", 
        "type": "text",
        "name": "fname",
        "inputmode":"text",
        "placeholder": "Lorem",
        "form_info": "",    
    },
    "lname": {
        "label_for": "lname",
        "text": "Efternavn", 
        "icon": "user_name_full.tpl", 
        "type": "text",
        "name": "lname",
        "inputmode":"text",
        "placeholder": "Ipsum",
        "form_info": "",    
    },
    "email": {
        "label_for": "email",
        "text": "Email", 
        "icon": "email.tpl", 
        "type": "email",
        "name": "email",
        "inputmode":"email",
        "placeholder": "loremipsum@mail.com",
        "form_info": "",    
    },
    "phone": {
        "label_for": "phone",
        "text": "Telefon nummer", 
        "icon": "phone.tpl", 
        "type": "tel",
        "name": "phone",
        "inputmode":"tel",
        "placeholder": "12 34 56 67",
        "form_info": "",    
    },
    "website_name": {
        "label_for": "website_name",
        "text": "Navn på din hjemmeside", 
        "icon": "pen_line.tpl", 
        "type": "text",
        "name": "website_name",
        "inputmode":"text",
        "placeholder": "Lorem-Ipsum.dk",
        "form_info": "",    
    },
    "website_url": {
        "label_for": "website_url",
        "text": "URL til din hjemmeside", 
        "icon": "www.tpl", 
        "type": "url",
        "name": "website_url",
        "inputmode":"url",
        "placeholder": "https://www.lorem-ipsum.dk",
        "form_info": "",    
    },
}

##############################
#   Routes
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
    return template('index', title="UNID Studio", user=user, first_name=first_name, last_name=last_name, username=username, header_nav_items=header_nav_items, footer_info=footer_info, section_landingpage_hero_content=section_landingpage_hero_content, unid_logo=unid_logo, selling_points=selling_points, social_media=social_media, ui_icons=ui_icons, form_inputs=form_inputs)


import routers.signup
import routers.login


##############################
#   CSS
@get("/app.css")
def _():
    return static_file('app.css', root='.')


##############################
try:
  import production # type: ignore
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=5000, debug=True, reloader=True)