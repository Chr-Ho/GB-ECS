# services/notification_service.py
# Notification Service

import datetime
from typing import List

class NotificationService:
    def __init__(self):
        # List to store notifications for overdue items
        self.notifications = []

    def check_for_overdue_items(self, equipment_list: List[dict]):
        # Iterate through the equipment list to check for overdue items
        for equipment in equipment_list:
            due_date = equipment.get("due_date")  # Assume each equipment item has a 'due_date' key
            if due_date:
                due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
                if due_date < datetime.datetime.now():
                    equipment_id = equipment.get("equipment_id", "Unknown ID")
                    self.create_overdue_notification(equipment_id)

    def create_overdue_notification(self, equipment_id: str):
        # Create a notification for the overdue equipment
        overdue_notification = {
            "message": f"Equipment {equipment_id} is overdue. Please return it immediately.",
            "equipment_id": equipment_id,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.notifications.append(overdue_notification)
        print(overdue_notification["message"])

    def get_notifications(self):
        # Return all notifications (for testing or logging)
        return self.notifications