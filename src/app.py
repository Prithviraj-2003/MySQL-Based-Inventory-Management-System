from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

# Flask app initialization
app = Flask(__name__)

# MySQL Database connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="inventory_system"
)
cursor = db.cursor()

# Home route - Display items
@app.route('/')
def index():
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return render_template('index.html', items=items)

# Add new item
@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    quantity = request.form['quantity']
    price = request.form['price']
    
    cursor.execute("INSERT INTO items (name, quantity, price) VALUES (%s, %s, %s)", (name, quantity, price))
    db.commit()
    
    return redirect(url_for('index'))

# Delete item
@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    cursor.execute("DELETE FROM items WHERE id=%s", (item_id,))
    db.commit()
    
    return redirect(url_for('index'))

# Update item
@app.route('/update/<int:item_id>', methods=['POST'])
def update_item(item_id):
    name = request.form['name']
    quantity = request.form['quantity']
    price = request.form['price']
    
    cursor.execute("UPDATE items SET name=%s, quantity=%s, price=%s WHERE id=%s", (name, quantity, price, item_id))
    db.commit()
    
    return redirect(url_for('index'))

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
