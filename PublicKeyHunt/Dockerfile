# Use an official Python 3 base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install system dependencies for bitcoinlib (if needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install bitcoinlib and other Python dependencies
RUN pip install --no-cache-dir bitcoinlib

# Expose a port (optional, if your app runs a server)
# EXPOSE 5000

# Set the default command to run your Python application (change as needed)
CMD ["python3"]
