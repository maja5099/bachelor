from bottle import post, request, response, redirect, template, get
import bcrypt
import os
from dotenv import load_dotenv
import dbconnection
import content

##############################
#   Content from content.py
header_nav_items = content.header_nav_items
footer_info = content.footer_info
unid_logo = content.unid_logo
selling_points = content.selling_points
social_media = content.social_media
ui_icons = content.ui_icons
section_profile_admin = content.section_profile_admin
section_profile_customer = content.section_profile_customer

@get("/profile")
def _():
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
    return template('profile', title="Din profil", user=user, section_profile_admin=section_profile_admin, section_profile_customer=section_profile_customer, first_name=first_name, last_name=last_name, username=username, header_nav_items=header_nav_items, footer_info=footer_info, unid_logo=unid_logo, selling_points=selling_points, social_media=social_media, ui_icons=ui_icons)