# services/equipment_service.py
# Equipment Management Service

class EquipmentManagementService:
    def __init__(self):
        # inventory keeps track of equipment data
        self.equipment = {}

    def check_out_equipment(self, user_id, equipment_id):
        # Check if the equipment exists in the inventory
        if equipment_id in self.equipment:
            equipment = self.equipment[equipment_id]
            if equipment['quantity'] > equipment['checked_out']:
                # Check out the equipment
                self.equipment[equipment_id]['checked_out'] += 1
                print(f'User {user_id} checked out 1 unit of {equipment_id}.')
            else:
                print(f'Sorry, all units of {equipment_id} are currently checked out.')
        else:
            print(f'{equipment_id} is not available in the inventory.')

    def check_in_equipment(self, user_id, equipment_id):
        # Check if the equipment exists in the inventory
        if equipment_id in self.equipment:
            equipment = self.equipment[equipment_id]
            if equipment['checked_out'] > 0:
                # Check in the equipment
                self.equipment[equipment_id]['checked_out'] -= 1
                print(f'User {user_id} returned 1 unit of {equipment_id}.')
            else:
                print(f'No units of {equipment_id} are currently checked out.')
        else:
            print(f'{equipment_id} is not recognized by the inventory.')
