from bottle import template, get, request, response
import master
import content
import os
import traceback

##############################
#   Content from content.py
header_nav_items = content.header_nav_items
footer_info = content.footer_info
unid_logo = content.unid_logo
selling_points = content.selling_points
social_media = content.social_media
ui_icons = content.ui_icons
pricing_default = content.pricing_default
pricing_accent = content.pricing_accent
section_profile_admin = content.section_profile_admin
section_profile_customer = content.section_profile_customer
form_inputs = content.form_inputs

@get("/contact")
def _():
    try:
        user = request.get_cookie("user", secret=os.getenv('MY_SECRET'))
        if user: 
            db = master.db()
            print("Type of user:", type(user))
            print("User:", user)
            username = user['username']
            first_name = user['first_name']
            last_name = user['last_name']
            user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
        else:
            user = None
            username = None
            first_name = None
            last_name = None
        return template('contact', title="UNID Studio - Kontakt", user=user, form_inputs=form_inputs, pricing_default=pricing_default, pricing_accent=pricing_accent, section_profile_admin=section_profile_admin, section_profile_customer=section_profile_customer, first_name=first_name, last_name=last_name, username=username, header_nav_items=header_nav_items, footer_info=footer_info, unid_logo=unid_logo, selling_points=selling_points, social_media=social_media, ui_icons=ui_icons)
    except Exception as e:
        error_message = str(e)
        traceback_message = traceback.format_exc()
        response.status = 500
        return f"<h1>Internal Server Error</h1><p>{error_message}</p><pre>{traceback_message}</pre>"
