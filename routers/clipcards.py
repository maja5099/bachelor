from bottle import template, get, post, request, response, delete, template
import master
import time
import uuid
from math import floor
from colored_logging import setup_logger
import content
import logging
import os



##############################
#   COLORED LOGGING
logger = setup_logger(__name__, level=logging.INFO)
logger.setLevel(logging.INFO)

##############################
#   Content from content.py
try:
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
    logger.success("Content imported successfully.")
except Exception as e:
    logger.error("Error importing content: %s", e)
finally:
    logger.info("Content import process completed.")


db = master.db()

@get('/profile/profile_customer_clipcard')
def clipcards():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_title, clipcard_price FROM card_types")
        clipcards = cursor.fetchall()
        cursor.close()
        template_path = find_template('profile_customer_clipcard', template_dirs)
        if template_path is None:
            return "Template not found."
            
        # Extract the relative path from views directory if necessary
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        return template(relative_path, clipcards=clipcards, pricing_default=pricing_default, pricing_accent=pricing_accent)
       
    except Exception as e:
        print("Error in clipcards:", e)
        return {"info": str(e)}
    
    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()

@get('/buy_clipcard/<clipcard_type>/<clipcard_price>')
def buy_clipcard(clipcard_type, clipcard_price):
    return template('buy_clipcard.html', clipcard_type=clipcard_type, clipcard_price=clipcard_price)

def minutes_to_hours_minutes(minutes):
    hours = floor(minutes / 60)
    remaining_minutes = minutes % 60
    return hours, remaining_minutes

@get('/profile/profile_admin_clipcard')
def admin_clipcards_get():
    try:
        db = master.db()
        template_path = find_template('profile_admin_clipcard', template_dirs)
        if template_path is None:
            return "Template not found."
            
        # Extract the relative path from views directory if necessary
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        cursor = db.cursor()
        
        cursor.execute("""
            SELECT clipcards.clipcard_id, clipcards.remaining_time, clipcards.time_used, clipcards.created_at, users.user_id, users.first_name, users.last_name, users.username, users.email, users.phone, customers.website_name, customers.website_url, card_types.clipcard_type_title
            FROM clipcards
            JOIN payments ON clipcards.clipcard_id = payments.clipcard_id
            JOIN users ON payments.user_id = users.user_id
            JOIN customers ON users.user_id = customers.customer_id
            JOIN card_types ON clipcards.clipcard_type_id = card_types.clipcard_type_id
            WHERE clipcards.is_active = "1";
        """)
        
        active_clipcards = cursor.fetchall()
        cursor.close()

        if not active_clipcards:
            print("No active clip cards.") 
            return template(relative_path, active_clipcards=[], active_customers=[])
        
        active_customers = [{'user_id': row['user_id'], 
                             'first_name': row['first_name'], 
                             'last_name': row['last_name'], 
                             'clipcard_id': row['clipcard_id']} 
                            for row in active_clipcards]

        for clipcard in active_clipcards:
            clipcard['time_used_hours'], clipcard['time_used_minutes'] = minutes_to_hours_minutes(clipcard['time_used'])
            clipcard['remaining_time_hours'], clipcard['remaining_time_minutes'] = minutes_to_hours_minutes(clipcard['remaining_time'])

            if clipcard['time_used_minutes'] > 0:
                clipcard['time_used_text'] = f"{clipcard['time_used_hours']} timer og {clipcard['time_used_minutes']} minutter"
            else:
                clipcard['time_used_text'] = f"{clipcard['time_used_hours']} timer"

            if clipcard['remaining_time_minutes'] > 0:
                clipcard['remaining_time_text'] = f"{clipcard['remaining_time_hours']} timer og {clipcard['remaining_time_minutes']} minutter"
            else:
                clipcard['remaining_time_text'] = f"{clipcard['remaining_time_hours']} timer"
       
        return template(relative_path, active_clipcards=active_clipcards, active_customers=active_customers)
    
    except Exception as e:
        print("Error in admin_clipcards:", e) 
        return {"info": str(e)}
    
    finally:
        if "db" in locals(): db.close()

@get('/profile/profile_admin_hour_registration')
def admin_clipcards_get():
    try:
        db = master.db()
        template_path = find_template('profile_admin_hour_registration', template_dirs)
        if template_path is None:
            return "Template not found."
            
        # Extract the relative path from views directory if necessary
        relative_path = template_path.replace('views/', '').replace('.tpl', '')

        cursor = db.cursor()
        
        cursor.execute("""
            SELECT clipcards.clipcard_id, clipcards.remaining_time, clipcards.time_used, clipcards.created_at, users.user_id, users.first_name, users.last_name, users.username, users.email, users.phone, customers.website_name, customers.website_url, card_types.clipcard_type_title
            FROM clipcards
            JOIN payments ON clipcards.clipcard_id = payments.clipcard_id
            JOIN users ON payments.user_id = users.user_id
            JOIN customers ON users.user_id = customers.customer_id
            JOIN card_types ON clipcards.clipcard_type_id = card_types.clipcard_type_id
            WHERE clipcards.is_active = "1";
        """)
        
        active_clipcards = cursor.fetchall()
        cursor.close()

        if not active_clipcards:
            print("No active clip cards.") 
            return template(relative_path, active_clipcards=[], active_customers=[])
        
        active_customers = [{'user_id': row['user_id'], 
                             'first_name': row['first_name'], 
                             'last_name': row['last_name'], 
                             'clipcard_id': row['clipcard_id']} 
                            for row in active_clipcards]

        for clipcard in active_clipcards:
            clipcard['time_used_hours'], clipcard['time_used_minutes'] = minutes_to_hours_minutes(clipcard['time_used'])
            clipcard['remaining_time_hours'], clipcard['remaining_time_minutes'] = minutes_to_hours_minutes(clipcard['remaining_time'])

            if clipcard['time_used_minutes'] > 0:
                clipcard['time_used_text'] = f"{clipcard['time_used_hours']} timer og {clipcard['time_used_minutes']} minutter"
            else:
                clipcard['time_used_text'] = f"{clipcard['time_used_hours']} timer"

            if clipcard['remaining_time_minutes'] > 0:
                clipcard['remaining_time_text'] = f"{clipcard['remaining_time_hours']} timer og {clipcard['remaining_time_minutes']} minutter"
            else:
                clipcard['remaining_time_text'] = f"{clipcard['remaining_time_hours']} timer"
       
        return template(relative_path, active_clipcards=active_clipcards, active_customers=active_customers)
    
    except Exception as e:
        print("Error in admin_clipcards:", e) 
        return {"info": str(e)}
    
    finally:
        if "db" in locals(): db.close()


template_dirs = ['components', 'elements', 'sections', 'utilities', 'profile', 'profile/admin']

def find_template(template_name, directories):
    base_path = 'views'
    for directory in directories:
        path = os.path.join(base_path, directory)
        print(f"Checking directory: {path}")
        for root, dirs, files in os.walk(path):
            print(f"Visited {root}")
            if f'{template_name}.tpl' in files:
                template_path = os.path.join(root, template_name + '.tpl')
                print(f"Found template at: {template_path}")
                return template_path
    print("Template not found")
    return None

@delete('/delete_clipcard/<clipcard_id>')
def delete_clipcard(clipcard_id):
    try:
        cursor = db.cursor()

        cursor.execute("SELECT * FROM clipcards WHERE clipcard_id = ?", (clipcard_id,))
        existing_clipcard = cursor.fetchone()
        if existing_clipcard is None:
            return {"info": f"The clip card with id {clipcard_id} does not exist."}

        if existing_clipcard["is_active"] == "0":
            return {"info": f"The clip card with id {clipcard_id} has already been deleted."}

        updated_at = int(time.time())
        deleted_at = int(time.time())

        cursor.execute("""
            UPDATE clipcards 
            SET updated_at = ?, deleted_at = ?, is_active = ? 
            WHERE clipcard_id = ?
        """, (updated_at, deleted_at, 0, clipcard_id))
        
        db.commit()

        return {"info": "The clip card has been deleted."}

    except Exception as e:
        db.rollback()
        print("Error in delete_clipcard:", e)
        return {"info": str(e)}

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'db' in locals(): db.close()


@post('/submit_task')
def submit_task():
    try:
        cursor = db.cursor()
        
        user_id = request.forms.get('customer')
        task_title = request.forms.get('title')
        task_description = request.forms.get('description')

        hours = int(request.forms.get('hours'))
        minutes = int(request.forms.get('minutes'))
        time_spent = hours * 60 + minutes
        created_at = int(time.time())

        print("Form data:")
        print("user_id:", user_id)
        print("task_title:", task_title)
        print("task_description:", task_description)
        print("hours:", hours)
        print("minutes:", minutes)

        cursor.execute("""
            SELECT payments.clipcard_id
            FROM payments
            JOIN clipcards ON payments.clipcard_id = clipcards.clipcard_id
            WHERE payments.user_id = ? AND clipcards.is_active = "1"
        """, (user_id,))
        result = cursor.fetchone()

        if result is None:
            return {"info": "No active clipcard found for the provided user_id."}

        clipcard_id = result["clipcard_id"]

        task_id = str(uuid.uuid4().hex) 
        cursor.execute("""
            INSERT INTO tasks (task_id, clipcard_id, customer_id, task_title, task_description, created_at, time_spent) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (task_id, clipcard_id, user_id, task_title, task_description, created_at, time_spent))

        db.commit()
        
        cursor.execute("""
            SELECT time_used, remaining_time
            FROM clipcards 
            WHERE clipcard_id = ?
        """, (clipcard_id,))
        time_data = cursor.fetchone()

        if time_data is not None and time_data["time_used"] is not None:
            time_used_minutes = int(time_data["time_used"]) + time_spent
            remaining_time_minutes = int(time_data["remaining_time"]) - time_spent
            cursor.execute("""
                UPDATE clipcards 
                SET time_used = ?, remaining_time = ? 
                WHERE clipcard_id = ?
            """, (time_used_minutes, remaining_time_minutes, clipcard_id))

            db.commit()

 
        return {"info": "Opgaven er blevet indsendt."}

    except Exception as e:
        db.rollback()
        print("Error in submit_task:", e)
        return {"info": str(e)}








