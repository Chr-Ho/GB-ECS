import sqlite3

# Function to initialize and create the SQLite database
def initialize_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    connection = sqlite3.connect('equipment_tracking.db')
    cursor = connection.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Create equipment table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            equipment_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            current_user_id INTEGER,
            FOREIGN KEY (current_user_id) REFERENCES users(user_id)
        )
    ''')

    # Create notifications table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notifications (
            notification_id INTEGER PRIMARY KEY,
            user_id INTEGER NOT NULL,
            message TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == '__main__':
    initialize_database()
    print("Database initialized and tables created.")

# Integrating SQLite with services
# Update services to use the SQLite database for CRUD operations
import sqlite3

class EquipmentManagementService:
    def check_out_equipment(self, user_id, equipment_id):
        connection = sqlite3.connect('equipment_tracking.db')
        cursor = connection.cursor()

        # Check if equipment is available
        cursor.execute("SELECT status FROM equipment WHERE equipment_id = ?", (equipment_id,))
        result = cursor.fetchone()
        if result and result[0] == 'available':
            # Update equipment status and assign to user
            cursor.execute("UPDATE equipment SET status = ?, current_user_id = ? WHERE equipment_id = ?", ('checked_out', user_id, equipment_id))
            connection.commit()
            connection.close()
            return True
        connection.close()
        return False

    def check_in_equipment(self, user_id, equipment_id):
        connection = sqlite3.connect('equipment_tracking.db')
        cursor = connection.cursor()

        # Check if the equipment is currently checked out by the user
        cursor.execute("SELECT status, current_user_id FROM equipment WHERE equipment_id = ?", (equipment_id,))
        result = cursor.fetchone()
        if result and result[0] == 'checked_out' and result[1] == user_id:
            # Update equipment status to available
            cursor.execute("UPDATE equipment SET status = ?, current_user_id = NULL WHERE equipment_id = ?", ('available', equipment_id))
            connection.commit()
            connection.close()
            return True
        connection.close()
        return False