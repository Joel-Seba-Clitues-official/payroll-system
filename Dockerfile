# Use official Python base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install flask

# Expose port (Flask default is 5000)
EXPOSE 5000

# Start the Flask app
CMD ["python", "app.py"]
