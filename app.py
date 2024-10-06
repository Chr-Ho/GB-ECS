# app.py
# Main file to run the Flask app. Import routes from api/routes.py and run the server from this file.

from flask import Flask
from api.routes import api_blueprint

app = Flask(__name__)

# Add this route to handle requests to the root URL
@app.route('/')
def home():
    return "Hello, World!"

app.register_blueprint(api_blueprint)  # Register routes from routes.py

if __name__ == '__main__':
    app.run(debug=True)

