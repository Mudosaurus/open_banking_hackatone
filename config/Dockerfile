# Use the official Python base image
FROM python:3.11

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Copy setup to initdb
COPY setup.sql /docker-entrypoint-initdb.d/

# Expose the port the app will run on
EXPOSE 80