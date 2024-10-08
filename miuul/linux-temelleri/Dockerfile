# Use the official Ubuntu base image
FROM ubuntu:latest

# Disable prompts from apt
ARG DEBIAN_FRONTEND=noninteractive

# Update the package repository and install basic utilities
RUN apt-get update && apt-get install -y \
    bash \
    coreutils \
    iputils-ping \
    net-tools \
    systemd \
    vim \
    curl \
    wget \
    man \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Set the default shell to bash
SHELL ["/bin/bash", "-c"]

# Start an interactive bash shell when the container runs
CMD ["bash"]
