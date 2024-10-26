# app.py
# Main file to run the Flask app. Import routes from api/routes.py and run the server from this file.

from flask import Flask, redirect, url_for, render_template, request
from api.routes import api_blueprint
from services.equipment_service import equipment_service
from services.user_service import user_service  # Import user_service

# Initialize the Flask application
app = Flask(__name__)

# Register the API blueprint with the app
app.register_blueprint(api_blueprint, url_prefix='/api')

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for checking out equipment
@app.route('/check_out')
def check_out_page():
    return render_template('check_out.html')

# Route for checking in equipment
@app.route('/check_in')
def check_in_page():
    return render_template('check_in.html')

# Route for updating inventory
@app.route('/update_inventory')
def update_inventory_page():
    return render_template('update_inventory.html')

# Route for viewing inventory
@app.route('/view_inventory')
def view_inventory_page():
    return render_template('view_inventory.html')

# Route for viewing equipment
@app.route('/view_equipment')
def view_equipment_page():
    return render_template('view_equipment.html')

# Route for viewing users
@app.route('/view_users')
def view_users_page():
    users = user_service.get_all_users()  # Fetch all users
    return render_template('view_users.html', users=users)

# Route for viewing equipment history
@app.route('/equipment_history')
def equipment_history_page():
    return render_template('equipment_history.html')

# Route for employee history search page
@app.route('/employee_history_search')
def employee_history_search():
    return render_template('employee_history_search.html')

# Route for manager login
@app.route('/manager_login', methods=['GET', 'POST'])
def manager_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Validate credentials
        if username == 'manager' and password == 'password':
            return redirect(url_for('manager_dashboard'))
        else:
            return "Invalid credentials, please try again.", 401
    
    return render_template('manager_login.html')

# Route for Employee History
@app.route('/employee_history', methods=['GET', 'POST'])
def employee_history():
    if request.method == 'POST':
        user_id = request.form['user_id']
        # Fetch employee equipment usage history
        history = equipment_service.get_equipment_history(user_id)
        if history:
            return render_template('employee_history.html', history=history)
        else:
            return "No history found for the provided User ID.", 404
    return render_template('employee_history_search.html')

# Route for manager dashboard
@app.route('/manager_dashboard')
def manager_dashboard():
    return render_template('manager_dashboard.html')

# Route for reporting exceptions
@app.route('/report_exception')
def report_exception_page():
    return render_template('report_exception.html')

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
