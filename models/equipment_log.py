# models/equipment_log.py
# Equipment Log Model

class EquipmentLog:
    def __init__(self, id, equipment_id, user_id, check_out_time, check_in_time):
        self.id = id
        self.equipment_id = equipment_id
        self.user_id = user_id
        self.check_out_time = check_out_time
        self.check_in_time = check_in_time