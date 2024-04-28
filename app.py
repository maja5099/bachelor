# 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
# https://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@github.com/maja5099/bachelor.git

from bottle import default_app, post, route, get, run, template, static_file
import git


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
#   Images
@get("/assets/<filename:re:.*\.(webp|png|jpg|gif|svg)>")
def _(filename):
    return static_file(filename, root="./assets")


##############################
#   Module level variables
unid_logo = {       
    "primary_logo": "primary_logo.svg",
    "logo_alt": "UNID Studio's logo",
}

selling_points = {       
    "first": {"icon": "heart.svg", "icon_alt": "Hjerte ikon", "text": "Tilfredshedsgaranti"},
    "second": {"icon": "discount.svg", "icon_alt": "Rabat ikon", "text": "Studierabat"},
    "third": {"icon": "pen.svg", "icon_alt": "Blyant ikon", "text": "Skræddersyet løsning"},
    "fourth": {"icon": "chat.svg", "icon_alt": "Taleboble", "text": "Hurtig kundeservice"}
}

header_links = [
    "Services & Priser",
    "Om UNID Studio",
    "Portfolio",
    "Cases",
    "Kontakt"
]

footer_info = [
    "UNID Studio © 2023",
    "All rights reserved",
    "CVR nr. 43924451",
]

social_media = {       
    "instagram": {"icon": "instagram.svg", "icon_alt": "Instagram's ikon", "link": "https://www.instagram.com/unid.studio/"},
    "linkedin": {"icon": "linkedin.svg", "icon_alt": "LinkedIn's ikon", "link": "https://www.linkedin.com/company/unid-studio/"},
}

section_landingpage_hero_content = {       
    "header_text": "Unikke & skræddersyede løsninger",
    "subheader_text": "Vi bestræber os på, at lave unikke og kvalitets løsninger som opfylder hver enkel kundes behov.",
    "button_text": "Kontakt os",
    "image": "digital_design.svg",
}


##############################
#   Routes
@route("/")
def index():
   return template('index', title="UNID Studio", header_links=header_links, footer_info=footer_info, section_landingpage_hero_content=section_landingpage_hero_content, unid_logo=unid_logo, selling_points=selling_points, social_media=social_media)


##############################
#   CSS
@get("/app.css")
def _():
    return static_file('app.css', root='.')


##############################
try:
  import production
  application = default_app()
except Exception as ex:
  print("Running local server")
  run(host="127.0.0.1", port=4000, debug=True, reloader=True)