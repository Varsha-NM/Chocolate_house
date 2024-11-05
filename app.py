
from flask import Flask, render_template, request, redirect,url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/flavors', methods=['GET', 'POST'])
def flavors():
    if request.method == 'POST':
        name = request.form['name']
        seasonal = 1 if 'seasonal' in request.form else 0  # Checkbox returns '1' if checked
        conn = get_db_connection()
        conn.execute('INSERT INTO flavors (name, seasonal) VALUES (?, ?)', (name, seasonal))
        conn.commit()
        conn.close()
        return redirect('/flavors')
    
    conn = get_db_connection()
    flavors = conn.execute('SELECT * FROM flavors').fetchall()
    conn.close()
    return render_template('flavors.html', flavors=flavors)



@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        ingredient = request.form['ingredient']
        quantity = request.form['quantity']
        conn = get_db_connection()
        conn.execute('INSERT INTO inventory (ingredient, quantity) VALUES (?, ?)', (ingredient, quantity))
        conn.commit()
        conn.close()
        return redirect('/inventory')
    
    conn = get_db_connection()
    inventory = conn.execute('SELECT * FROM inventory').fetchall()
    conn.close()
    return render_template('inventory.html', inventory=inventory)

@app.route('/suggestions', methods=['GET', 'POST'])
def suggestions():
    if request.method == 'POST':
        customer_name = request.form['customer_name']
        suggestion = request.form['suggestion']
        conn = get_db_connection()
        conn.execute('INSERT INTO suggestions (customer_name, suggestion) VALUES (?, ?)', (customer_name, suggestion))
        conn.commit()
        conn.close()
        return redirect('/suggestions')
    
    conn = get_db_connection()
    suggestions = conn.execute('SELECT * FROM suggestions').fetchall()
    conn.close()
    return render_template('suggestions.html', suggestions=suggestions)

@app.route('/allergies', methods=['GET', 'POST'])
def allergies():
    if request.method == 'POST':
        item_name = request.form['item_name']
        allergy = request.form['allergy']
        conn = get_db_connection()
        conn.execute('INSERT INTO allergies (item_name, allergy) VALUES (?, ?)', (item_name, allergy))
        conn.commit()
        conn.close()
        return redirect('/allergies')
    
    conn = get_db_connection()
    allergies = conn.execute('SELECT * FROM allergies').fetchall()
    conn.close()
    return render_template('allergies.html', allergies=allergies)

if __name__ == '__main__':
    app.run(debug=True)