# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install required libraries
RUN pip install --no-cache-dir numpy pandas matplotlib seaborn scikit-learn \
    tensorflow keras jupyterlab

# Expose the port for JupyterLab
EXPOSE 8888

# Define the command to run JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
