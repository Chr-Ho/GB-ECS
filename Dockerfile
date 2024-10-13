# Dockerfile

FROM python:3.10-slim

# Create a user for Celery worker security
RUN useradd -m celeryuser

# Set working directory in container
WORKDIR /app

# Copy requirements.txt first for caching purpose
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .

# Set environment variable for Flask app
ENV FLASK_APP=app.py

# Set the user to run subsequent commands
#USER celeryuser

# Default command (for the web container)
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]
