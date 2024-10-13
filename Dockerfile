# Dockerfile

# Use the official Python 3.10 image as the base image
FROM python:3.10-slim

# Create a non-root user and set it as the default user
RUN useradd -m celeryuser
#USER celeryuser

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port that Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["flask", "run"]
