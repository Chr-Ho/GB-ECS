# app.py
# Main file to run the Flask app. Import routes from api/routes.py and run the server from this file.

from flask import Flask, render_template
from api.routes import api_blueprint

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

# Main entry point
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)