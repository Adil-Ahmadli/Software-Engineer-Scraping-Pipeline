# Use the official Python image as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files to the working directory
COPY . .

# Change directory to the jobs_project folder
WORKDIR /app/jobs_project

# Set the entrypoint command to run the Scrapy spider
CMD scrapy crawl jobs_spider