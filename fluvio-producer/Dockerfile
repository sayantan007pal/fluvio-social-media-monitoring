# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container
COPY app/ .

# Install Fluvio and other dependencies
RUN pip install fluvio requests textblob

# Run the Fluvio producer (adjust command as necessary)
CMD ["python", "producer.py"]
