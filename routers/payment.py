from bottle import post, request, redirect, template, response
import uuid
import time
import master
import os

def get_current_user():
    try:
        user_info = request.get_cookie('user', secret=os.getenv('MY_SECRET'))
        if not user_info:
            return None
        
        username = user_info.get('username')
        if username:
            db = master.db()
            current_user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            db.close()
            return current_user
        else:
            return None
    except Exception as e:
        print(e)
        return None

db = master.db()

@post('/process_payment')
def process_payment():
    try:
        current_user = get_current_user()
        if not current_user:
            raise Exception('User information not found in session.')

        user_id = current_user['user_id']
        if not user_id:
            raise Exception('User ID not found.')

        clipcard_price = request.forms.get('clipcard_price')
        amount_paid = clipcard_price 
        payment_id = str(uuid.uuid4())
        clipcard_id = str(uuid.uuid4())
        created_at = int(time.time())
        updated_at = int(time.time())
        is_active = 1
        clipcard_type_title = request.forms.get('clipcard_type')
        time_used = 0
        
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_id, clipcard_type_time FROM card_types WHERE clipcard_type_title = ?", (clipcard_type_title,))
        row = cursor.fetchone()

        if not row:
            raise Exception('Clipcard type not found')

        clipcard_type_id = row['clipcard_type_id'] 
        remaining_time = row['clipcard_type_time']  

        cursor.execute("INSERT INTO payments (payment_id, user_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
                       (payment_id, user_id, clipcard_id, amount_paid, created_at))
        
        cursor.execute("INSERT INTO clipcards (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       (clipcard_id, clipcard_type_id, time_used, remaining_time, created_at, updated_at, is_active)) 
        
        db.commit()
        cursor.close()
        
        print("Payment processed successfully.")
        
        return template("confirmation", title="Confirmation", payment_id=payment_id, amount_paid=amount_paid, created_at=created_at)
    
    except Exception as e:
        print(e)
        return {"info":str(e)}
