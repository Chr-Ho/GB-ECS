# models/inventory_item.py
# Inventory Item Model

class InventoryItem:
    def __init__(self, id, item_name, warehouse_location, quantity):
        self.id = id
        self.item_name = item_name
        self.warehouse_location = warehouse_location
        self.quantity = quantity