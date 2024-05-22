from bottle import template, get, post, request
import master
import time
import uuid
import sqlite3


db = master.db()

@get('/customer_clipcards')
def clipcards():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_title, clipcard_price FROM card_types")
        clipcards = cursor.fetchall()
        cursor.close()
        return template("customer_clipcards", clipcards=clipcards)
    
    except Exception as e:
        print("Error in clipcards:", e)
        return {"info": str(e)}

@get('/buy_clipcard/<clipcard_type>/<clipcard_price>')
def buy_clipcard(clipcard_type, clipcard_price):
    return template('buy_clipcard.html', clipcard_type=clipcard_type, clipcard_price=clipcard_price)

@get('/admin_clipcards')
def admin_clipcards():
    try:
        cursor = db.cursor()
        
        cursor.execute("""
            SELECT clipcards.clipcard_id, clipcards.remaining_time, clipcards.time_used, users.user_id, users.first_name, users.last_name, users.username, users.email, customers.website_name, customers.website_url, card_types.clipcard_type_title
            FROM clipcards
            JOIN payments ON clipcards.clipcard_id = payments.clipcard_id
            JOIN users ON payments.user_id = users.user_id
            JOIN customers ON users.user_id = customers.customer_id
            JOIN card_types ON clipcards.clipcard_type_id = card_types.clipcard_type_id
            WHERE clipcards.is_active = "TRUE";
        """)
        
        active_clipcards = cursor.fetchall()
        cursor.close()

        if not active_clipcards:
            print("Ingen aktive klippekort.") 
            return template("admin_clipcards", active_clipcards=[], active_customers=[])

        active_customers = [{'user_id': row['user_id'], 
                             'first_name': row['first_name'], 
                             'last_name': row['last_name'], 
                             'clipcard_id': row['clipcard_id']} 
                            for row in active_clipcards]
        
       
        return template("admin_clipcards", active_clipcards=active_clipcards, active_customers=active_customers)
    
    except Exception as e:
        print("Error in admin_clipcards:", e) 
        return {"info": str(e)}
    
    finally:
        if "db" in locals(): db.close()



@post('/delete_clipcard/<clipcard_id>')
def delete_clipcard(clipcard_id):
    try:
        cursor = db.cursor()

        updated_at = int(time.time())
        deleted_at = int(time.time())

        cursor.execute("""
            UPDATE clipcards 
            SET updated_at = ?, deleted_at = ?, is_active = ? 
            WHERE clipcard_id = ?
        """, (updated_at, deleted_at, "FALSE", clipcard_id))
        
        db.commit()

        return "Klippekortet er blevet opdateret."

    except Exception as e:
        db.rollback()
        print("Error in delete_clipcard:", e)
        return {"info": str(e)}

    finally:
        if "db" in locals(): db.close()

from bottle import request

@post('/submit_task')
def submit_task():
    try:
        db.row_factory = sqlite3.Row 
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
            WHERE payments.user_id = ? AND clipcards.is_active = "TRUE"
        """, (user_id,))
        result = cursor.fetchone()

        print("SQL query result:", result)

        if result is None:
            return {"info": "No active clipcard found for the provided user_id."}

        clipcard_id = result["clipcard_id"]

        task_id = str(uuid.uuid4().hex) 
        cursor.execute("""
            INSERT INTO tasks (task_id, clipcard_id, customer_id, task_title, task_description, created_at, time_spent) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (task_id, clipcard_id, user_id, task_title, task_description, created_at, time_spent))

        db.commit()
        
        return "Opgaven er blevet indsendt."

    except Exception as e:
        db.rollback()
        import traceback
        print("Error in submit_task:", traceback.format_exc())
        return {"info": str(e)}

    finally:
        if "db" in locals(): db.close()

