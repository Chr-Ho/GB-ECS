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
    user_id = request.form.get('user_id')  # Extract user_id from form data
    equipment_id = request.form.get('equipment_id')  # Extract equipment_id from form data

    if not user_id or not equipment_id:
        return jsonify({'error': 'Missing user_id or equipment_id'}), 400

    success = equipment_service.check_in_equipment(user_id, equipment_id)
    if success:
        return jsonify({'message': f'Equipment {equipment_id} successfully checked in by user {user_id}.'}), 200
    else:
        return jsonify({'error': 'Failed to check in equipment.'}), 400

# Route for updating inventory
@api_blueprint.route('/update_inventory', methods=['POST'])
def update_inventory():
    data = request.get_json()
    item_id = data.get('item_id')
    quantity = data.get('quantity')
    warehouse_location = data.get('warehouse_location')
    
    if not item_id or quantity is None or not warehouse_location:
        return jsonify({'error': 'item_id, quantity, and warehouse_location are required'}), 400
    
    result = inventory_service.update_inventory(item_id, quantity, warehouse_location)
    if result:
        return jsonify({'message': 'Inventory updated successfully'}), 200
    else:
        return jsonify({'error': 'Inventory could not be updated'}), 400

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
