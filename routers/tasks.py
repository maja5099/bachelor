from bottle import run, get
import json
import dbconnection


# Endpoint for at hente kundens fornavn og efternavn
@get('/get_customers')
def get_customers():
    db = dbconnection.db()
    cursor = db.cursor()
    cursor.execute("SELECT u.first_name, u.last_name FROM users u JOIN payments p ON u.user_id = p.user_id JOIN clipcards c ON p.clipcard_id = c.clipcard_id WHERE c.is_active = 1")
    customers = cursor.fetchall()
    db.close()
    return json.dumps(customers)

# Endpoint for at servere HTML-formularen
@get('/')
def serve_form():
    with open('form.html', 'r') as file:
        return file.read()


