# Use the official Ubuntu image as a base
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /app

# Update package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 python3-pip  postgresql-client && \
    rm -rf /var/lib/apt/lists/*


# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

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