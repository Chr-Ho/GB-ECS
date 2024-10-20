# models/equipment_log.py
# Equipment Log Model

class EquipmentLog:
    def __init__(self, log_id, equipment_id):
        self.id = log_id
        self.equipment_id = equipment_id

        import csv
        with open('Equipmentlist.csv', mode='r+') as file:
            writer = csv.writer(file)
            reader = csv.reader(file)
            for row in reader:
                print(row)
            writer.writerow(['equipment_id', 'id'])  # Ensure consistent naming

