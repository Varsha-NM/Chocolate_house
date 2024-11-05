import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create tables for flavors, inventory, suggestions, and allergies
cursor.execute('''
CREATE TABLE IF NOT EXISTS flavors (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    seasonal BOOLEAN NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    id INTEGER PRIMARY KEY,
    ingredient TEXT NOT NULL,
    quantity INTEGER NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS suggestions (
    id INTEGER PRIMARY KEY,
    customer_name TEXT NOT NULL,
    suggestion TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS allergies (
    id INTEGER PRIMARY KEY,
    item_name TEXT NOT NULL,
    allergy TEXT NOT NULL
)
''')

conn.commit()
conn.close()
