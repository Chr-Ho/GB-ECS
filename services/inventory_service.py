# services/inventory_service.py
# Inventory Management Service

import sqlite3

class InventoryManagementService:
    
    def update_inventory (self, equipment_id, name, quantity, warehouse_location):
        connection = sqlite3.connect('equipment_tracking.db')
        cursor = connection.cursor()
        
        result = cursor.exectute("SELECT equipment_id FROM equipment where equipment_id = ?", (equipment_id))
        if result.fetchone() == equipment_id:
            cursor.execute("UPDATE equipment SET quantity = ? , SET warehouse_location = ? , SET name = ? WHERE equipment_id = ?", (quantity, warehouse_location, name, equipment_id))
        else:
            return("Item not found")
        connection.commit()
        connection.close()
        
    def get_inventory(self, equipment_id):
        connection = sqlite3.connect('equipment_tracking.db')
        cursor = connection.cursor()
        
        item = InventoryItem()
        
        result = cursor.exectue("SELECT eqipment_id, name, quantity, warehouse_location FROM equipment WHERE equipment_id = ?"(equipment_id))
        result.fetchone()
        
        item.id = result[0]
        item.name = result[1]
        item.quantity = result[2]
        item.warehouse_location = result[3]
