import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('equipment_tracking.db')
cursor = conn.cursor()

# Drop existing tables if they exist
cursor.execute('DROP TABLE IF EXISTS equipment')
cursor.execute('DROP TABLE IF EXISTS inventory')
cursor.execute('DROP TABLE IF EXISTS users')

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    user_name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Create the inventory table
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    item_id TEXT PRIMARY KEY,
    item_name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    warehouse_location TEXT NOT NULL
)
''')

# Create the equipment table
cursor.execute('''
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id TEXT PRIMARY KEY,
    equipment_name TEXT NOT NULL,
    status TEXT NOT NULL,
    current_user_id INTEGER,
    FOREIGN KEY (current_user_id) REFERENCES users(user_id)
)
''')

# Import users from users.csv
with open('users.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            user_id = int(row['user_id'])  # Ensure user_id is an integer
            user_name = str(row['user_name'])
            email = str(row['email'])
            cursor.execute('INSERT OR REPLACE INTO users (user_id, user_name, email) VALUES (?, ?, ?)',
                           (user_id, user_name, email))
        except ValueError as e:
            print(f"Skipping row due to data format error in users.csv: {e} for row {row}")

# Import inventory from inventorylist.csv
with open('inventorylist.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            item_id = str(row['item_id'])  # Ensure item_id is a string
            item_name = str(row['item_name'])  # Ensure consistent naming
            quantity = int(row['quantity'])  # Ensure quantity is an integer
            location = str(row['warehouse_location'])
            cursor.execute('INSERT OR REPLACE INTO inventory (item_id, item_name, quantity, warehouse_location) VALUES (?, ?, ?, ?)',
                           (item_id, item_name, quantity, location))  # Ensure consistent naming
        except ValueError as e:
            print(f"Skipping row due to data format error in inventorylist.csv: {e} for row {row}")

# Import equipment from equipmentlist.csv
with open('equipmentlist.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            equipment_id = str(row['equipment_id'])  # Now treating equipment_id as a string
            equipment_name = str(row['equipment_name'])
            status = str(row['status'])
            current_user_id = int(row['current_user_id']) if row['current_user_id'] else None  # Ensure current_user_id is an integer or None
            cursor.execute('INSERT OR REPLACE INTO equipment (equipment_id, equipment_name, status, current_user_id) VALUES (?, ?, ?, ?)',
                           (equipment_id, equipment_name, status, current_user_id))
        except ValueError as e:
            print(f"Skipping row due to data format error in equipmentlist.csv: {e} for row {row}")

# Commit changes and close the connection
conn.commit()
conn.close()
