# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the necessary Python packages
RUN pip install requests

# Define environment variables with default values
ENV URL=http://example.com
ENV PERIOD=60
ENV TIMEOUT=10.0

# Run the Python script when the container launches
CMD ["python", "get_request.py"]
