# services/inventory_service.py
# Inventory Management Service

import sqlite3

class InventoryManagementService:
    
    def update_inventory(self, item_id, item_name, quantity, warehouse_location):
        try:
            connection = sqlite3.connect('equipment_tracking.db')
            cursor = connection.cursor()
            
            # Check if the item exists in the inventory
            cursor.execute("SELECT item_id FROM inventory WHERE item_id = ?", (item_id,))
            result = cursor.fetchone()
            
            if result:
                # Update the inventory item
                cursor.execute("UPDATE inventory SET item_name = ?, quantity = ?, warehouse_location = ? WHERE item_id = ?",
                               (item_name, quantity, warehouse_location, item_id))
                connection.commit()
                return True  # Indicate success
            else:
                return "Item not found"  # Indicate that the item does not exist

        except sqlite3.Error as e:
            # Log the error for debugging purposes
            print(f"Database error occurred while updating inventory: {e}")
            return False  # Indicate failure
        finally:
            connection.close()  # Ensure the connection is closed

    def get_inventory(self, item_id):
        try:
            connection = sqlite3.connect('equipment_tracking.db')
            cursor = connection.cursor()
            
            # Query the inventory for the specified item_id
            cursor.execute("SELECT item_id, item_name, quantity, warehouse_location FROM inventory WHERE item_id = ?", (item_id,))
            item = cursor.fetchone()
            
            if item:
                return {
                    'item_id': item[0],
                    'item_name': item[1],
                    'quantity': item[2],
                    'warehouse_location': item[3]
                }
            else:
                return None  # Item not found

        except sqlite3.Error as e:
            # Log the error for debugging purposes
            print(f"Database error occurred while retrieving inventory: {e}")
            return None  # Indicate failure
        finally:
            connection.close()  # Ensure the connection is closed
