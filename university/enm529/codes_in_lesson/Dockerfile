FROM python:3.11

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install scikit-learn pandas numpy matplotlib seaborn

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
CMD ["echo", "Hello, World!"]