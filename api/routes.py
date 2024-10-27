import sqlite3
from flask import Blueprint, request, jsonify
from services.equipment_service import EquipmentManagementService
from services.inventory_service import InventoryManagementService
from services.notification_service import NotificationService

# Create a Blueprint for the API routes
api_blueprint = Blueprint('api', __name__)

# Initialize services
equipment_service = EquipmentManagementService()
inventory_service = InventoryManagementService()
notification_service = NotificationService()

# Route for checking out equipment
@api_blueprint.route('/check_out', methods=['POST'])
def check_out():
    user_id = request.form.get('user_id')  # Extract user_id from form data
    equipment_id = request.form.get('equipment_id')  # Extract equipment_id from form data

    if not user_id or not equipment_id:
        return jsonify({'error': 'Missing user_id or equipment_id'}), 400

    success = equipment_service.check_out_equipment(user_id, equipment_id)
    if success:
        return jsonify({'message': f'Equipment {equipment_id} successfully checked out by user {user_id}.'}), 200
    else:
        return jsonify({'error': 'Failed to check out equipment.'}), 400

# Route for checking in equipment
@api_blueprint.route('/check_in', methods=['POST'])
def check_in():
    user_id = request.form.get('user_id')
    equipment_id = request.form.get('equipment_id')

    print(f"Received user_id: {user_id}, equipment_id: {equipment_id}")  # Debugging line

    if not user_id or not equipment_id:
        return jsonify({'error': 'Missing user_id or equipment_id'}), 400

    success = equipment_service.check_in_equipment(user_id, equipment_id)
    if success:
        return jsonify({'message': f'Equipment {equipment_id} successfully checked in by user {user_id}.'}), 200
    else:
        return jsonify({'error': 'Failed to check in equipment.'}), 400

# Route for updating inventory
@api_blueprint.route('/update_inventory', methods=['POST'])
def update_inventory(self, item_id, item_name, quantity, warehouse_location):
    try:
        connection = sqlite3.connect('equipment_tracking.db')
        cursor = connection.cursor()
        
        # Check if the item exists in the inventory
        cursor.execute("SELECT item_id FROM inventory WHERE item_id = ?", (item_id,))
        result = cursor.fetchone()
        
        if result:
            # Update the inventory item
            cursor.execute("UPDATE inventory SET item_name = ?, quantity = ?, warehouse_location = ? WHERE item_id = ?",
                           (item_name, quantity, warehouse_location, item_id))
            connection.commit()
            return True  # Indicate success
        else:
            return "Item not found"  # Indicate that the item does not exist

    except sqlite3.Error as e:
        # Log the error for debugging purposes
        print(f"Database error occurred while updating inventory: {e}")
        return False  # Indicate failure
    finally:
        connection.close()  # Ensure the connection is closed

# Route for viewing inventory
@api_blueprint.route('/get_inventory/<string:item_id>', methods=['GET'])
def get_inventory(item_id):
    result = inventory_service.get_inventory(item_id)
    if result:
        return jsonify(result), 200
    else:
        return jsonify({'error': 'Item not found'}), 404
    
# Route for sending notifications
@api_blueprint.route('/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    
    if not user_id or not message:
        return jsonify({'error': 'user_id and message are required'}), 400
    
    notification_service.send_notification(user_id, message)
    return jsonify({'message': 'Notification sent successfully'}), 200

# Route for reporting equipment exceptions
@api_blueprint.route('/report_exception', methods=['POST'])
def report_exception():
    data = request.get_json()
    equipment_id = data.get('equipment_id')
    status = data.get('status')

    if not equipment_id or not status:
        return jsonify({'error': 'equipment_id and status are required'}), 400

    # Here you would log the exception report in your database
    # For demonstration, we will just print it
    print(f"Reporting exception for equipment {equipment_id} with status '{status}'.")

    # Send notification to the inventory manager
    notification_service.send_exception_notification(equipment_id, status)

    return jsonify({'message': 'Exception report generated successfully.'}), 200
