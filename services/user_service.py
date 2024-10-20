import sqlite3

class UserService:
    def get_all_users(self):
        try:
            connection = sqlite3.connect('equipment_tracking.db')
            cursor = connection.cursor()
            
            # Query to fetch all users
            cursor.execute("SELECT user_id, user_name, email FROM users")
            users = cursor.fetchall()
            
            # Convert to a list of dictionaries for easier access in the template
            return [
                {
                    'user_id': item[0],
                    'user_name': item[1],
                    'email': item[2]
                }
                for item in users
            ]
        except sqlite3.Error as e:
            print(f"Database error occurred while retrieving users: {e}")
            return []
        finally:
            connection.close()  # Ensure the connection is closed

user_service = UserService()  # Instantiate the service