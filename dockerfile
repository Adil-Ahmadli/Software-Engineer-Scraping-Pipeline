# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Search for postgresql-client package
RUN apt-cache search postgresql-client

# Install PostgreSQL client tools
RUN sudo apt-get install -y --no-install-recommends postgresql-client

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the waiting script into the container at /app
COPY wait_for_postgres.sh .

# Make the script executable
RUN chmod +x wait_for_postgres.sh

# Copy the rest of your Scrapy project into the container at /app
COPY . .

# Change directory to the jobs_project folder
WORKDIR /app/jobs_project

# Command to wait for PostgreSQL and then run Scrapy crawl
CMD ["../wait_for_postgres.sh", "scrapy", "crawl", "jobs"] 