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

equipment_service = EquipmentService()  # Instantiate the service

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
