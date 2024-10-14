# services/notification_service.py
# Notification Service

class NotificationService:
    
    def send_notification(self, user_id, message):
        print(user_id, message)
        
    def notify_overdue_equipment(self, equipment_id, user_id):
        if overdue:#placeholder
            self.send_notification(user_id, "Equipment overdue")
