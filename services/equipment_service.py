# services/equipment_service.py
# Equipment Management Service

import sqlite3
import datetime

class EquipmentService:
    def __init__(self):
        self.equipment_history = []

    def log_equipment_usage(self, user_id, equipment_id, action):
        # Log check-out/check-in events
        self.equipment_history.append({
            'user_id': user_id,
            'equipment_id': equipment_id,
            'action': action,
            'date': datetime.datetime.now()
        })

    def get_equipment_history(self, user_id):
        # Retrieve all history related to the provided user_id
        return [record for record in self.equipment_history if record['user_id'] == user_id]

class EquipmentManagementService(EquipmentService):
    def check_out_equipment(self, user_id, equipment_id):
        try:
            connection = sqlite3.connect('equipment_tracking.db')
            cursor = connection.cursor()

            # Ensure user_id is an integer and equipment_id is a string
            user_id = int(user_id)  # Make sure user_id is an integer
            equipment_id = str(equipment_id)  # Treat equipment_id as a string

            # Check if equipment is available for check-out
            cursor.execute("SELECT status FROM equipment WHERE equipment_id = ?", (equipment_id,))
            result = cursor.fetchone()

            if result and result[0] == 'in':
                # Update equipment status and assign it to the user
                cursor.execute("UPDATE equipment SET status = ?, current_user_id = ? WHERE equipment_id = ?",
                               ('checked_out', user_id, equipment_id))
                connection.commit()
                
                # Log the equipment usage
                self.log_equipment_usage(user_id, equipment_id, 'check_out')
                
                return True
            else:
                # Equipment might not be available for check-out
                return False

        except sqlite3.Error as e:
            # Log the error for debugging purposes
            print(f"Database error occurred while checking out equipment: {e}")
            return False
        finally:
            connection.close()  # Ensure the connection is closed

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

    def get_all_equipment(self):
        try:
            connection = sqlite3.connect('equipment_tracking.db')
            cursor = connection.cursor()
            
            # Query to fetch all equipment
            cursor.execute("SELECT equipment_id, equipment_name, status, current_user_id FROM equipment")
            equipment = cursor.fetchall()
            
            # Convert to a list of dictionaries for easier access in the template
            return [
                {
                    'equipment_id': item[0],
                    'equipment_name': item[1],
                    'status': item[2],
                    'current_user_id': item[3]
                }
                for item in equipment
            ]
        except sqlite3.Error as e:
            print(f"Database error occurred while retrieving equipment: {e}")
            return []
        finally:
            connection.close()  # Ensure the connection is closed

equipment_service = EquipmentManagementService()  # Instantiate the service