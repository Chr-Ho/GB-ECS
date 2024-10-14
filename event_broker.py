# event_broker.py
# Implement a basic event broker for managing events

import queue
from services.equipment_service import EquipmentManagementService
from services.inventory_service import InventoryManagementService
from services.notification_service import NotificationService

class EventBroker:
    def __init__(self):
        # Initialize the queue to hold events
        self.event_queue = queue.Queue()
        # Initialize services
        self.equipment_service = EquipmentManagementService()
        self.inventory_service = InventoryManagementService()
        self.notification_service = NotificationService()

    def trigger_event(self, event_type, data):
        # Adds an event with a specific type and data to the queue
        self.event_queue.put((event_type, data))

    def process_events(self):
        # While queue is not empty, process each event
        while not self.event_queue.empty():
            # Gets next event from the queue
            event_type, data = self.event_queue.get()
            
            # Processes the events
            # check_out_equipment
            if event_type == 'check_out':
                success = self.equipment_service.check_out_equipment(data['user_id'], data['equipment_id'])
                if success:
                    print(f"Equipment {data['equipment_id']} successfully checked out by user {data['user_id']}")
                    self.notification_service.send_notification(data['user_id'], f"You have successfully checked out equipment {data['equipment_id']}")
                else:
                    print(f"Failed to check out equipment {data['equipment_id']} by user {data['user_id']}")
            # check_in_equipment
            elif event_type == 'check_in':
                success = self.equipment_service.check_in_equipment(data['user_id'], data['equipment_id'])
                if success:
                    print(f"Equipment {data['equipment_id']} successfully checked in by user {data['user_id']}")
                    self.notification_service.send_notification(data['user_id'], f"You have successfully checked in equipment {data['equipment_id']}")
                else:
                    print(f"Failed to check in equipment {data['equipment_id']} by user {data['user_id']}")
            # update_inventory
            elif event_type == 'update_inventory':  # Fixed typo here
                success = self.inventory_service.update_inventory(data['item_id'], data['quantity'], data['warehouse_location'])
                if success:
                    print(f"Inventory for item {data['item_id']} updated with quantity {data['quantity']}")
                else:
                    print(f"Failed to update inventory for item {data['item_id']}")
            else:
                print(f"Unknown event type: {event_type}")
                    
         