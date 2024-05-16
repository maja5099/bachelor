from bottle import template, get
import dbconnection

db = dbconnection.db()

@get('/customer_clipcards')
def clipcards():
    try:
        cursor = db.cursor()
        cursor.execute("SELECT clipcard_type_title, clipcard_price FROM card_types")
        clipcards = cursor.fetchall() 
        cursor.close()
        return template("customer_clipcards", clipcards=clipcards)
    
    except Exception as e:
        print(e)
        return {"info":str(e)}

@get('/buy_clipcard/<clipcard_type>/<clipcard_price>')
def buy_clipcard (clipcard_type, clipcard_price):
    return template('buy_clipcard.html', clipcard_type=clipcard_type, clipcard_price=clipcard_price)



@get('/admin_clipcards')
def admin_clipcards():
    try:
        db = dbconnection.db()
        cursor = db.cursor()
        
        cursor.execute("""
            SELECT clipcards.*, payments.amount_paid, payments.created_at, users.username, users.first_name, users.last_name, users.email, customers.website_name, customers.website_url, card_types.clipcard_type_title
                FROM clipcards
                JOIN payments ON clipcards.clipcard_id = payments.clipcard_id
                JOIN users ON payments.user_id = users.user_id
                JOIN customers ON users.user_id = customers.customer_id
                JOIN card_types ON clipcards.clipcard_type_id = card_types.clipcard_type_id
                WHERE clipcards.is_active = "TRUE";
        """)

        
        active_clipcards = cursor.fetchall()
        
        return template("admin_clipcards", active_clipcards=active_clipcards)
    
    except Exception as e:
        print(e)
        return {"info":str(e)}
    
    finally:
        if "db" in locals(): db.close()