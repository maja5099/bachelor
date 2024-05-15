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




