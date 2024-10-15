FROM ubuntu:latest

# Install necessary packages
RUN apt-get update -y && \
    apt-get install -y nano curl vim wget git unzip tar python3

# Add a new user
RUN useradd -m developer01

# Set the working directory
WORKDIR /home/developer01

# Switch to the new user
USER developer01

# Copy the current directory contents into the container at /home/developer01
COPY app.py .

# Define the command to run the Python script
CMD ["python3", "app.py"]