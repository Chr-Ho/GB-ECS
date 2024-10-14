
import csv
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('equipment_tracking.db')
cursor = conn.cursor()

# Create the users table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
)
''')

# Create the inventory table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS inventory (
    item_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    location TEXT NOT NULL
)
''')

# Create the equipment table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS equipment (
    equipment_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
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
            name = str(row['name'])
            email = str(row['email'])
            cursor.execute('INSERT OR REPLACE INTO users (user_id, name, email) VALUES (?, ?, ?)',
                           (user_id, name, email))
        except ValueError as e:
            print(f"Skipping row due to data format error in users.csv: {e} for row {row}")

# Import inventory from inventorylist.csv
with open('inventorylist.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            item_id = str(row['id'])  # Ensure item_id is a string
            name = str(row['item_name'])
            quantity = int(row['quantity'])  # Ensure quantity is an integer
            location = str(row['warehouse_location'])
            cursor.execute('INSERT OR REPLACE INTO inventory (item_id, name, quantity, location) VALUES (?, ?, ?, ?)',
                           (item_id, name, quantity, location))
        except ValueError as e:
            print(f"Skipping row due to data format error in inventorylist.csv: {e} for row {row}")

# Import equipment from equipmentlist.csv
with open('equipmentlist.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            equipment_id = str(row['equipment_id'])  # Now treating equipment_id as a string
            id = str(row['name'])
            status = str(row['status'])
            current_user_id = int(row['current_user_id']) if row['current_user_id'] else None  # Ensure current_user_id is an integer or None
            cursor.execute('INSERT OR REPLACE INTO equipment (equipment_id, name, status, current_user_id) VALUES (?, ?, ?, ?)',
                           (equipment_id, name, status, current_user_id))
        except ValueError as e:
            print(f"Skipping row due to data format error in equipmentlist.csv: {e} for row {row}")

# Commit changes and close the connection
conn.commit()
conn.close()
