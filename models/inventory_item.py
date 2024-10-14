# models/inventory_item.py
# Inventory Item Model

class InventoryItem:
    def __init__(self, id, item_name, warehouse_location, quantity):
        self.id = id
        self.item_name = item_name
        self.warehouse_location = warehouse_location
        self.quantity = quantity

        import csv
        with open('Inventorylist.csv', mode='r+') as file:
            writer = csv.writer(file)
            reader = csv.reader(file)
            for row in reader:
                print(row)
            writer.writerow(['id', 'item_name', 'warehouse_location', 'quantity'])  



