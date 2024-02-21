# Use an official Python runtime as a base image
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the application code from the project directory to /app inside the container
COPY ../../app/application/ .
# Command to run your application
CMD ["python", "main.py"]
