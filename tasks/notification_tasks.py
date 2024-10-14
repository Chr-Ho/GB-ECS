# tasks/notification_tasks.py
# Define tasks for overdue notifications

from celery import Celery

# Initialize Celery app
app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def notify_if_overdue(user_id, equipment_id):
    print(f"Sending overdue notification for Equipment ID: {equipment_id} to User ID: {user_id} ")
