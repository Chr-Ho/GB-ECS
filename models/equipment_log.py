# models/equipment_log.py
# Equipment Log Model

class EquipmentLog:
    def __init__(self, id, equipment_id):
        self.id = id
        self.equipment_id = equipment_id

        import csv
        with open('Equipmentlist.csv', mode='r,w') as file:
            writer = csv.writer(file)
            reader = csv.reader(file)
            for row in reader:
                print(row)
            writer.writerow(['id', 'equipment_id']) 
        