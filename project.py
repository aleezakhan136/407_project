from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

# Connect to the smoochez database
db = mysql.connector.connect(
    host="localhost",
    user="root",         # ← Replace with your MySQL username
    password="Yassumalz5702!", # ← Replace with your MySQL password
    database="smoochez"
)

cursor = db.cursor()

# Route to show the order form
@app.route('/')
def order_form():
    return render_template('contact us.html')  # Make sure to update this HTML too

# Route to handle form submission
@app.route('/submit-order', methods=['POST'])
def submit_order():
    item_type = request.form['item_type']
    item_description = request.form.get('item_description', '')
    name = request.form['name']
    email = request.form['email']
    address_line1 = request.form['address_line1']
    address_line2 = request.form.get('address_line2', '')
    city = request.form['city']
    state = request.form['state']
    zip_code = request.form['zip_code']

    sql = """
        INSERT INTO orders 
        (item_type, item_description, name, email, address_line1, address_line2, city, state, zip_code)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (item_type, item_description, name, email,
              address_line1, address_line2, city, state, zip_code)

    try:
        cursor.execute(sql, values)
        db.commit()
        return "Order submitted successfully!"
    except mysql.connector.Error as err:
        return f"Error: {err}"

if __name__ == '__main__':
    app.run(debug=True)
