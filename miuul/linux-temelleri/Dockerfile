# I want to create a ubuntu container to test some linux commands
# I will use ubuntu image as base image
FROM ubuntu:latest

# I will install some packages
RUN apt-get update && apt-get install -y \
    iputils-ping \
    net-tools \
    iproute2 \
    dnsutils \
    curl \
    wget \
    vim \
    nano \
    git \
    && rm -rf /var/lib/apt/lists/*

# I will create a new user
RUN useradd -ms /bin/bash miuul

# I will switch to miuul user
USER miuul

# I will set the working directory
WORKDIR /home/miuul

# I will create a new file
RUN touch test.txt

# I will run a command
CMD ["echo", "Hello World!"]
