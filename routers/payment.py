from bottle import post, request, redirect
import uuid
import datetime
import dbconnection
import os

db = dbconnection.db()

# Hent customer_id fra databasen baseret på user_id
def get_customer_id_from_user_id(user_id):
    cursor = db.cursor()
    cursor.execute("SELECT customer_id FROM customers WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        return result[0]
    else:
        return None

@post('/process_payment')
def process_payment():
    try:
        # Hent brugeroplysninger fra cookien
        user_info = request.get_cookie('user', secret=os.getenv('MY_SECRET'))
        if not user_info:
            raise Exception('User information not found in cookie.')
        
        # Hent brugerens ID fra brugeroplysningerne
        user_id = user_info['user_id']
        if not user_id:
            raise Exception('User ID not found in cookie.')
        
        # Hent customer_id baseret på user_id
        customer_id = get_customer_id_from_user_id(user_id)
        if not customer_id:
            raise Exception('Customer ID not found for user ID: {}'.format(user_id))
        
        clipcard_price = request.forms.get('clipcard_price')
        amount_paid = clipcard_price 
        payment_id = str(uuid.uuid4())
        clipcard_id = str(uuid.uuid4())
        created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO payments (payment_id, customer_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
                       (payment_id, customer_id, clipcard_id, amount_paid, created_at))
        db.commit()
        cursor.close()
        
        redirect('/confirmation')
    
    except Exception as e:
        print(e)
        return {"info":str(e)}
