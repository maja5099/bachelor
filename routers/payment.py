from bottle import post, request, redirect
import uuid
import datetime
import dbconnection
import os

# Funktion til at hente den aktuelle bruger baseret på sessionoplysninger
def get_current_user():
    try:
        # Hent brugeroplysninger fra cookien
        user_info = request.get_cookie('user', secret=os.getenv('MY_SECRET'))
        if not user_info:
            return None
        
        # Her kan du tilpasse din logik til at hente brugeren baseret på cookien
        # For eksempel kan du bruge brugernavnet til at finde brugeren i databasen
        username = user_info.get('username')
        if username:
            db = dbconnection.db()
            current_user = db.execute("SELECT * FROM users WHERE username = ? LIMIT 1", (username,)).fetchone()
            db.close()
            return current_user
        else:
            return None
    except Exception as e:
        print(e)
        return None

db = dbconnection.db()

@post('/process_payment')
def process_payment():
    try:
        # Hent den aktuelle bruger
        current_user = get_current_user()
        if not current_user:
            raise Exception('User information not found in session.')

        # Hent brugerens ID
        user_id = current_user['user_id']
        if not user_id:
            raise Exception('User ID not found.')

        clipcard_price = request.forms.get('clipcard_price')
        amount_paid = clipcard_price 
        payment_id = str(uuid.uuid4())
        clipcard_id = str(uuid.uuid4())
        created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        cursor = db.cursor()
        cursor.execute("INSERT INTO payments (payment_id, user_id, clipcard_id, amount_paid, created_at) VALUES (?, ?, ?, ?, ?)",
                       (payment_id, user_id, clipcard_id, amount_paid, created_at))
        db.commit()
        cursor.close()
        
        redirect('/confirmation')
    
    except Exception as e:
        print(e)
        return {"info":str(e)}
