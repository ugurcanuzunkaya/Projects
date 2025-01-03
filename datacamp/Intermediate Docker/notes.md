# Intermediate Docker Course - Datacamp

## Docker Refresher

- Docker is a container runtime
- Designated to run and manage various containerized applications on Windows, Linux, and Mac
- Can run containers using pre-built images, or create our own
- Dockerfiles are text files used to Docker container images
- Containers are instances of a given Docker image

### Docker Commands

- `docker run` - Run a container
- `docker stop` - Stop a container
- `docker build` - Build a container image
- `docker --help` - Get help on Docker commands
- `docker <command> --help` - Get help on a specific Docker command

### Temporary Containers

- Docker containers are usually created with `docker run`
- Containers remain even after stopping / exiting
- Often want to run a container instance and remove it immediately upon exit
  - Development
  - Testing
  - Scripts
- `docker run --rm` - Run a container and remove it upon exit
- `docker run --rm alpine:latest /bin/sh` - Run an Alpine container and remove it upon exit. Referenced as 'clean-up' or 'remove'

### docker ps

- `docker ps` - List running containers
- Used for determining name, id, status, and other attributes of containers on a given machine running Docker
- Use the `-a` flag to list all containers, including stopped ones. `docker ps -a`

## Mounting The Host Filesystem

### Container filesystems

- Container instances each have their own filesystem
  - Based off the image the container was created with
- Any changes are tied to that specific container instance
- Any changes are maintaned across restarts
  - For that instance only
- New containers only have the data in the image, not instance specific changes
- Isolated from the host filesystem
- [Docker Volumes](container_filesystem.png)

### Sharing Files or Directories

- Can attach specific files or directories from the host to a container
- Allows for persistence of data, wihout maintaining a specific container instance
- Can upgrade to new version but safely keep data/changes
- Known as 'bind-mount'
- Can be read-only or read/write
- Note: When files or directories are attached to a container, they are not accessible to the host until the container is shutdown

### Bind Mounts

- bind-mounts most often use the `-v` flag
- `-v <source>:<destination>` - Bind mount a file or directory from the host to the container
- Multiple '-v' flags can be used to attach multiple files or directories. At least 16 bind-mounts per container but it varies.
- Can also use the `--mount` flag for more advanced options
- Note: bind-mount hides any content already present in the destionation directory in the container
- `docker run -v /host/path:/container/path alpine:latest /bin/sh` - Run an Alpine container with a bind-mount from the host to the container
- `docker run -v ~/html:/var/www/html nginx:latest` - Run an Nginx container with a bind-mount from the host to the container
- `docker run
    -v ~/pgdata:/opt/data \
    -v ~/pg.conf:/etc/pg.conf \
    postgresql:latest` - Run a PostgreSQL container with two bind-mounts from the host to the container

## Persistent Volumes

- Volumes are an option to store data in Docker, unrelated to the container image or host filesystem
- Are managed from the command line (or API)
- Can share with multiple containers
- You need to handle data access and permissions but considerably more powerful than bind-mount.
- Higher performance than file share /bind mounts
- Exist until removed

### Managing Volumes

- `docker volume` - Manage volumes
- `docker volume create <volumename>`- Create a volume with a specific name
- `docker volume ls` or `docker volume list` - List all volumes
- `docker volume inspect <volumename>` - Get detailed information about a volume. Show metadata about the volume, including its name, mount point(on the host / destination), and various options for the volume.
- `docker volume rm <volumename>` - Remove a volume
- Example:
  - `docker volume create myvolume` - Create a volume named 'myvolume'.
  - `docker volume ls` - List all volumes, including 'myvolume'.
  - `docker volume inspect myvolume` - Get detailed information about 'myvolume'.
  - `docker volume rm myvolume` - Remove 'myvolume'.

### Attaching Volume

- Uses '-v' flag
- `docker run -v <volumename>:<destination path>:<options>` - Attach a volume to a container
- Volume name is name of existing volume
- Destionation path is the location the volume will be mounted (such as /data)
- Options are optional comma-seperated list of values such as 'ro' for read-only.
- Example: `docker run -v myvolume:/data alpine:latest /bin/sh` - Run an Alpine container with a volume attached to /data
- '--mount' flag can also be used for more advanced options. Exists ass with bind-mounts.

### Drivers

- Methods of storing Docker volumes.
- Can include:
  - Local filesystem (default)
  - NFS (Unix filesharing)
  - SMB / CIFS (Windows filesharing)
  - Other drivers: Remote systems, backup devices, and so forth.

## Networking Refresher

- A computer network consists of systems communicating via a defined method
- Varying levels of communication, physical or logical, referred to as protocols
- Common physical networks include Ethernet and WiFi
- Logical networking includes TCP/IP, HTTP, and SMTP
- Networks are defined in various layers or levels. Often referred to as a networking stack

### Networking Terms

- Host
  - General term for a computer
- Network
  - Group of hosts
- Interface
  - Actual connection from a host to a network, such as Ethernet or WiFi
  - Can be virtual, meaning entirely in software
- LAN
  - Local Area Network, or set of computers at a given location
- VLAN
  - Virtual LAN, or a software LAN

### Internet PRotocal

- IP
  - Internet protocol, method to connect between networks using IP addresses
- IPv4
  - Version of IP supporting 4.2 billion addresses, currently exhausted
  - IPv4: 10.10.10.1
- IPv6
  - Newer version of IP, supporting 2^128 addresses, still being deployed
  - IPv6: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

###  TCP/UDP

- TCP
  - Transmission Control Protocol, used to reliably communicate between hosts on IP networks
- UDP
  - User Datagram Protocol, used to communicate between hosts on IP where communication is not required.

### Ports

- Port
  - Addresses services on a given host, a value between 0 and 65535, used to communicate between hosts via TCP or UDP
  - Ports below 1024 are typically reserved for privileged accounts like root.
  - Ports above 1024 are usually ephemeral or temporaray ports.
  - Application listen on a port. This means it waits for new connections on that port and responds to clients from it.

### Application Protocols

- HTTP/HTTPS
  - Application protocol, defaulting to TCP port 80 for web communication. Secure version on TCP 443
- SMTP
  - Email transfer protocol, defaulting to TCP port 25
- SNMP
  - Simple Network Management Protocol, defaulting to UDP port 161

### Docker and Networking

- Can communicate between containers
- Can communicate with the host system
- Depending on settings can communicate with external hosts
- Typical communcation is handled by exposing ports from container to host
- Acts like a translation between containers and hosts

### Docker and IP

- Containers can have IP addresses
- Use `ìfconfig <interface>`or `ip addr show <interface>` from within container to find addresses
- Use `ping -c <x> <host>` to verify connectivity. Replace `<x>` with number of pings and `<host>` with the host to ping. Example: `ping -c 4 myhost`
- Interfaces here are virtual between the host and the containers.
- [IP Address](ip_adresses.png)

## Making Network Services Available in Docker

### Network Services

- Network services listen on a given port
- Only one program can listen on an IP:port combo at a given time
  - For example, 10.1.2.3:80 would be listening on 10.1.2.3 on port 80
- Consider trying to debug different versions of a web server that listens on port 80
  - Could only run one copy of the application at a time given that it listens only on that port

### Contaierized Services

- Wrapping application in a container means that each container can now listen on that port (as the IP:port combo is different, each container has a different IP)
- Can have multiple copies of the containers running at once
- But how to connect to container's version of application from the host?

### Port Mapping

- The answer is the use of port mapping, or port forwarding/translation
- Port mapping takes a connection to a given IP:port and automatically forwards it to a different IP:port combo
- In this case, we could map an unused port on our host and point it to port 80 on the container(s)
- The Docker engine can handle this automatically if we configure it to
- Example: [Port Mapping](port_mapping.png). We have 3 containers and make them accessible to the host or systems that can reach the host, we can use port mapping to connect ports 5501, 5502, and 5503 to point to port 80 on each container.

### Enabling Port Mapping

- To enable port mapping on a given container, we use the `docker run` command and '-p' flag
- `-p <hostport>:<containerport>` - Map a port from the host to the container. `-p 5501:80` would map port 5501 on the host to port 80 on the container
- Can have multiple '-p' flags for different ports
- Example: `docker run -p 5501:80 nginx` - Run an Nginx container and map port 5501 on the host to port 80 on the container

## Exposing Ports with Dockerfiles

### Exposing Services

- `EXPOSE` command in a Dockerfile
- Defines which ports the container will use at runtime
- Can be defined as `<number>`, `<number>/tcp`, or `<number>/udp`
  - Such as `EXPOSE 80`, `EXPOSE 80/tcp`, or `EXPOSE 80/udp`
  - The default is TCP
- Multiple entries can be used
- Used as a documentation method. Letting the Docker user know which ports should be exposed from within the container

### Using the -p/-P flags

- Still requires use of '-p' or '-P' options to `docker run` to make the ports available outside the container
- The '-P' option will automatically map an ephemeral port to the exposed port(s). Must use `docker ps -a` to see which ports were mapped
- Using `-p<host port>:<container port>` allows use of specific ports.
- Example: `docker run -p 5501:80 nginx` - Run an Nginx container and map port 5501 on the host to port 80 on the container

### EXPOSE Example

- Example Dockerfile:

```Dockerfile
FROM python:3.11-slim
ENTRYPOINT ["python", "-mhhtp.server"]
EXPOSE 8000
```

- This Dockerfile uses the Python 3.11 slim image
- Create a container from the image and run it. `docker run pyserver`
- Print the state of the container. `docker ps -a`
- If we try to access this port from the host, it will not be reachable as we have not defined what host port to use.

### Making Ports Reachable

- Automatically map temporary port from host to the container
- `docker run -P pyserver` - automatically map a port from the host to the container. '-p' uses manual port mapping.
- Use `docker ps -a` to see which ports were mapped

### Finding Exposed Ports

- `docker inspect`- Provide a lot of information about a container, including exposed ports
- `docker inspect <id>` - Get detailed information about a container. Replace `<id>` with the container ID
- The output is in JSON format. Note that typically this information is overkill but may be useful in cases of many exposed ports or more extended troubleshooting situations.

## Docker Networks

- Docker has extensive networking options
- Can create networks to communicate between containers, host, and external systems
- Will cover various commands to interact with networks

### Docker Networking Types

- Docker supports different networking types, using drivers
  - bridge: Default network driver, allows connections out, connections in if exposed
  - host: Allows full communication between host and containers
  - none: Isolate container from network communications
  - Many others, including custom drives

### Working with Docker Networks

- Several commands:
  - `docker network` - Manage networks
  - `docker network <command> --help` - Get help on a specific network command
  - `docker network ls` - List networks
  - `docker network create <networkname>` - Create a network
  - `docker network rm <networkname>` - Remove a network

### Network Example

- Create a Docker network
  - `docker network create mynetwork` - It will return id of the network
  - `docker network ls` - List networks, including 'mynetwork'. You will see the shorter id of the network

### Attaching Containers to Networks

- How to connect container to a network?
- `docker run --network <networkname> <imagename>` - Attach a container to a network
- Example: `docker run --network mynetwork alpine:latest /bin/sh` - Run an Alpine container and attach it to 'mynetwork'
- Can aslo connect containers later
  - `docker network connect <networkname> <containername>` - Connect a container to a network

### Docker Network Inspect

- How to check details of a network?
- `docker network inspect <networkname>` - Get detailed information about a network
- Provides configuration info and IP addresses assigned to containers

## Review

- You learned about Docker networking, which allows containers to communicate with each other, the host, and external systems. Here are the key points you covered:

- Types of Docker Networks:

  - Bridge Driver: The default network driver that allows communication between containers on the same network and to the internet.
  - Host Driver: Enables full communication between the host and containers, but with potential security implications.
  - None Driver: Completely isolates the container from any network, useful for testing untrusted applications.

- Key Docker Network Commands:
  - docker network ls: Lists all Docker networks on the host.
  - docker network create mynetwork: Creates a new network named "mynetwork".
  - docker network rm networkname: Removes a specified network.

- Connecting Containers to Networks:
  - Use docker run --network mynetwork ubuntu bash to create a container connected to "mynetwork".
  - Use docker network connect mynetwork containerid to connect an existing container to "mynetwork".

- Inspecting Networks:
  - docker network inspect mynetwork: Provides detailed configuration of the network, including IP ranges and assigned IP addresses.

- Example command to create and list networks:
  - docker network create mynetwork
  - docker network ls

- You also practiced creating, adding containers to, and inspecting Docker networks, as well as identifying unused IP ranges and understanding which networks cannot be removed.

##  Optimizing Docker Images

### Docker Image

- Docker images are the base of a given container
- Holds all content initially available to a container instance
- Concerns:
  - Tempting to add all potentially needed components to an image
  - Size becomes large / unwieldy
  - Difficult to handle security / updates due to dependency issues
  - Harder to combine containers without wasting space / bandwidth
- Recommendations
  - Split containers to the smallest level needed
  - Easier to combine multiple containers later vs. building a single large image
  - Like
    - Building with reusable components
    - vs. building from scratch each time
  - Updates to specific software only affect containers using that image instead of all containers needing the update
  - Can optimize for size, making use and distribution much easier

###  Example

- Consider a data engineering project using the following software:
  - Postgresql database
  - Python ETL software
  - Web server software
- Possible to use a single image, but we would need to update the image each time we had an update to the ETL or web server setup
- What would happen if we needed to add another web server?

### Minimized Containers

- Better options with Docker
- Split each into its own container
  - Postgresql database container
  - Python ETL components
  - Web server
- Can build an optimized configuration for our use, and can add / remove components as needed

```bash
docker run -d postgresql:latest
docker run -d nginx:latest
...
```

###  Determining Image Size

- Using `docker images` to determine image size
- Shows individual image details, including size
- More in-depth options covered later.
- `docker images --help` - Get help on the `docker images` command
- `docker images --digests` - Show image digests. A digest is a unique identifier for an image, based on the image contents.

## Understanding Layers

### Docker Layers

- Docker images are made up of layers
- A layer generally references a change or command within a Dockerfile
- Layers can be cached / reused
- The order of commands within a Dockerfile can affect whether layers are reused
- [Docker Layers](docker_layers.png)

### Why do we care about layers?

- Reusability
  - Faster build times
  - Taking up less space

### Docker Image Inspect

- `docker image inspect` - Get detailed information about an image
- `docker image inspect <imagename>` - Get detailed information about a specific image
- The `RootFS:Layers` section provides details about layers in a given Docker image

###  Example Docker Image Inspect

- `docker image inspect postgres:latest` - Get detailed information about the Postgres image
- [Docker Image Inspect Example](docker_image_inspect_example.png)

### jq Command-Line Tool

- Sometimes difficult to analyze the results from `docker image inspect`
- `jq` is a command-line tool is used to read JSON data, like what's returned from `docker image inspect`
- Can use `jq` to query data

### jq Recipes with Docker

- Method to see just a specific section, for example the `RootFS` data
  - `docker image inspect <id> | jq '.[0] | .RootFS'`
- Method to count number of layers using `jq`
  - `docker image inspect <id> | jq '.[0] | {LayerCount: .RootFS.Layers | length}'`

## Multi-stage Builds

### Single-stage Builds

- Typical Docker images are created using a single FROM command
- Each addition to the source image adds space and makes its management more complex
- Consider an application that must be compiled prior to use
  - You can add all the necessary components to the image, compile it, and then configure the final image for use
  - This often leaves superfluous content in the image even if it is not used
  - This increases the size of the image and makes it harder to manage.

### Multi-stage Builds Overview

- Multi-stage builds use multiple containers
- Typically has one or more build stages
- Final components are copied into a final container image
- The build stages are then removed automatically
  - Saving space and minimizing the size of the container image
- Uses some additional syntax in the Dockerfile
  - `AS <alias>` - Define a stage with a given alias
  - `COPY --from=<alias>` - Copy from a given stage

### Multi-stage Build Example

- Example Dockerfile:

```yaml
# Create initial build stage
FROM ubuntu AS stage1
# Install compiler and compile code
RUN apt install gcc -y
...
RUN make

# Start new stage to create final image
FROM alpine-base
# Copy from first stage to final
COPY --from=stage1 /data_app /data_app
# Run application on container start
CMD ["data_app"]
```

- We can provide a different alias other than 'stage1'.

## Multi-platform Builds

### Multi-platform

- It references two different aspects:
  - An operating system (OS) like Linux, Windows, or MacOS
  - A CPU architecture like x86, ARM, or PowerPC. x64_64 or amd64, arm64, arm7
- Usually referred to as 'os/cpu', such as 'linux/amd64'

###  Creating Multi-platform Builds

- Is built on multi-stage build behaviour
- The inital / build stage tends to use cross-compilers and relies on the architecture of the host system
- It's possible to create multi-platform builds seperately, such as for linux/amd64 and linux/arm64, it's not recommended.
- Final stage uses the architecture / OS for the intended target and copies any compiled binaries in place.

### Multi-platform Dockerfile Options

- Build stage uses the `--platform=$BUILDPLATFORM` flag
  - `$BUILDPLATFORM` represents the platform of the host running the build
- Sometimes uses the 'ARG' directive
  - Passes local environment variables into the Docker build system
  - In this case, 'TARGETOS' and 'TARGETARCH' are used to define the target platform
  - `ARG TARGETOS TARGETARCH`
  - The environment variables at the host level can be defined previously or using the `env` command

### Multi-platform Dockerfile Example

- Example Dockerfile:

```yaml
# Initial stage, using local platform
FROM --platform=$BUILDPLATFORM golang:1.21 AS build
# Copy source into place
WORKDIR /src
COPY . .
# Pull the environment variables from the host
ARG TARGETOS TARGETARCH
# Compile the code using the ARG variables
RUN env GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o /final/app .

# Create container and load the cross-compiled code
FROM alpine
COPY --from=build /final/app /bin
```

### Building a Multi-platform Build

- To create a multi-platform build, instead of using `docker build`, we must use `docker buildx` with assorted options
- `docker buildx` provides more commands and capabilities than `docker build` including the option to specify a platform
- `docker buildx build --platform linux/amd64,linux/arm64 -t multi-platform-app .` - Build a multi-platform image for both amd64 and arm64
- Prior to running the build, we must also have a new builder container present. This is done with the `docker buildx create --bootstrap --use` command

## Review of Last Learning Session 0

- Multi-Platform Concept: Multi-platform builds target different OS types (e.g., Linux, Windows, macOS) and CPU types (e.g., x86_64, arm64).
- Platform Definition: Platforms are defined as ostype/cputype, such as linux/amd64 or macos/arm64.
- Build Stages: Multi-platform builds use multi-stage builds with cross-compilers to compile code for different target platforms.
- Dockerfile Options:
  - --platform=$BUILDPLATFORM: Ensures the base image matches the host platform.
  - ARG TARGETOS TARGETARCH: Passes target platform components to the build process.

- Example Dockerfile snippet:

```yaml
FROM --platform=$BUILDPLATFORM golang:1.21 AS build
WORKDIR /app
COPY . .
ARG TARGETOS TARGETARCH
RUN GOOS=$TARGETOS GOARCH=$TARGETARCH go build -o myapp

FROM alpine
COPY --from=build /app/myapp /myapp
```

- Building the Image: Use docker buildx for multi-platform builds:
  - `docker buildx build --platform linux/amd64,linux/arm64 -t multi-platform-app .`

- You also practiced ordering build steps and creating a Docker image for the linux/arm64 platform.

## Introduction to Docker Compose

### What is Docker Compose

- Docker Compose is a tool for defining, managing and running multi-container Docker applications
- Additional command-line tool for Docker
- Specify containers, networking, and storage volumes in a single file
  - compose.yml or compose.yaml
  - May be named docker-compose.yml or docker-compose.yaml
- Easy to share / demo applications

### Example compose.yml

- Example Docker Compose file:

```docker
# Define the services
services:
    # Define the container(s), by name
    webapp:
        image: "webapp"
        # Optionally, define the port forwarding
        ports:
            - "8000:5000"
    # Define any other containers required
    redis:
        image: "redis:alpine"
```

### Starting an Application

- `docker compose up` - Start the application. `docker-compose up` is also valid for older systems
  - `docker compose -f <yaml> up` - Start the application using a specific YAML file
  - `docker compose up -d` - Start the application in detached mode

### Checking Status of Applications

- `docker compose ls` - List the application(s), the status of the required containers, and the config file used to start the application.

### Stopping an Application

- `docker compose down` - Stop the application. `docker-compose down` is also valid for older systems
  - `docker compose -f <yaml> down` - Stop the application using a specific YAML file

## Creating compose.yaml Files

###  YAML

- Yet Another Markup Language
  - YAML Ain't Markup Language
- Text file, but spacing matters
- Used in many development scenarios for configuration
- Rules can be tricky, mainly keep entries lined up as in examples
- Maintaining indentation is crucial
- A YAML skeleton will be provided when needed, but be aware of the formatting requirements if you need to create one from scratch
- [YAML Example](yaml_example.png)

### Main Sections

- Different sections handle different components
- `services:` - List the containers to load
- `networks:` - Handles networking definitions
- `volumes:` - Controls any volume mounting
- `configs:` - Handles configuration options without custom images
- `secrets:` - Provides options to handle passwords, tokens, API keys, etc.
- Documentain: [Docker Compose File Reference](https://docs.docker.com/compose/compose-file/)

###  Services Section

- Defines all required resources for the application
- Primarily specifies the containers and images to be used
- Extensive options available, but only apply to the individual container(s)
- Indention is applied as needed
- First subsection is the name of each component, followed by the settings

###  Example Services

- `container_name:` - Assigned name of the container otherwise it's random
- `image:` - The image to use for the container
- `ports:` - Contains a list of any port mapping required
- Followed by next resources required
- [Services Example](services_example.png)

## Review of Last Learning Session 1

- You learned about creating Docker Compose files using YAML, a human-readable text format where indentation matters. Docker Compose allows you to manage multi-container applications with a single configuration file. Here are the key points you covered:

  - YAML Basics: YAML stands for "YAML Ain't Markup Language" and is used for configuration due to its readability. Proper indentation is crucial.

  - Docker Compose Sections:

    - services: The only required section, listing all containers for the application.
    - networks: Optional, for specific networking configurations.
    - volumes: Optional, for defining shared storage.
    - configs: Optional, for specifying configuration details.
    - secrets: Optional, for managing passwords, tokens, or API keys.
    - Services Section: Defines all required resources, including container names, images, and settings.

  - Here is an example of a compose.yaml file you worked on:

        ```yaml
        services:
        primary:
            container_name: webapp
            image: test_app:latest
            ports:
            - "8000:8000"
        ```

  - This example sets up a single service named primary with a container named webapp, using the test_app:latest image and mapping port 8000 on the host to port 8000 in the container.

## Dependicies and troubleshooting in Docker Compose

###  Dependicies

- Dependencies define the order of resource startup
- Resources (containers) may require other resources
- Example web application
  - Database container `postgresql` must start first
  - Then the `python_app`
  - Finally, the `nginx` web server
  - [Example](dependencies_example.png)

### depends_on

- Dependencies defined using the `depends_on` attribute
- Can chain dependencies as per example
- Or, can have multiple dependencies per resource if required
- Order of the `compose.yaml` file does not matter
- [Example](dependencies_yaml_example.png)

### Shutting down applications

- Shutting down an application occurs in reverse order
- Stops `nginx` resource
- Then stops the `python_app` resource
- And finally the `postgresql` resource

### Other options

- Docker Compose provides other options for dependencies
- `condition:` - defines how to decide when resource is ready
  - `service_started` - Resource has started normally
    - Default behavior
  - `service_completed_successfully` - Resource ran to completion, such as a initial configuration /etc
  - `service_healthy` - Resource meets a criteria defined by `healthcheck`. The healthcheck is a defined method, such as accessing a specific webpage or verifying a TCP port answers a connection request.

### Docker Compose Troubleshooting Tools

- Docker Compose has additional troubleshooting tools
- `docker compose logs` - Gather output from all resources in applicaiton
- `docker compose logs <resourcename>` - Gather output from a specific resource

###  docker compose top

- `docker compose top` - Show status of resources within an application

## Review of Last Learning Session 2

- You learned about managing dependencies and troubleshooting in Docker Compose, which is crucial for ensuring that multi-container applications start and run smoothly. Here are the key points you covered:

- Dependencies in Docker Compose: You explored how dependencies define the order in which containers start. For example, a web application might need a database container to start first. This is managed using the depends_on attribute.
- Dependency Conditions: You learned about different conditions for dependencies:
  - service_started: The default condition indicating a service has started.
  - service_completed_successfully: Indicates a service has completed its task.
  - service_healthy: Indicates a service has passed a health check.
- Shutting Down Containers: Containers shut down in reverse order of their startup dependencies.
- Troubleshooting Tools: You used docker-compose logs to gather logs from all containers and docker-compose top to check the status of running containers.
- Here’s an example of a docker-compose.yml file with dependencies:

    ```yaml
    services:
    web:
        image: custom_app
        depends_on:
        - redis
    llm:
        image: openai-llm:14
        depends_on:
        - web
    forwarder:
        image: fwd_proxy/latest
    redis:
        image: redis:latest
        depends_on:
        forwarder:
            condition: service_healthy
    ```

- Keep practicing these concepts to master Docker Compose!

## Creating a Data Service within Docker

###  Data Sharing

- `docker run -v <host directory>:<container directory>` - Share data between host and container
  - `-v ~/hostdata:/containerdata` - Share data between host and container

### Data Sharing in compose.yaml

- Also present in 'compose.yaml' files

```yaml
services:
    resource:
        name: resource1
        # Section named volumes
        volumes:
            - ~/hostdata:/containerdata
```

- List syntax here means each indented line starting with a dash.
- We can use as many entries as needed for all required bind mounts.

###  Networks

- `docker run --network <networkname>` - Attach a container to a network
  - `docker run --network mynetwork` - Attach a container to 'mynetwork'
- Also present in 'compose.yaml' files

```yaml
services:
    resource:
        name: resource1
        # Section named networks
        networks:
            net1:   #<network_name>:
```

### Port Mapping in compose.yaml

- `docker run -p <hostport>:<containerport>` - Map a port from the host to the container
  - `docker run -p 8000:8000`- Map port 8000 on the host to port 8000 on the container
- Also present in 'compose.yaml' files

```yaml
services:
    resource:
        name: resource1
        # Section named ports
        ports:
            - "8000:8000"  #<hostport>:<containerport>
```

- We can map as many ports as needed.

### docker inspect

- Determine information about provisioned containers
- `docker inspect <containername>` - Get detailed information about a container. `docker inspect <id>` is also valid.
- Provides various levels of information
  - `Mounts:` - Provides mounted data information
  - `NetworkSettings:` - Network information
    - `NetworkSettings:Networks` - Shows the Docker network(s) connection details

```yaml
"Config": {
    "Mounts": [...]
    ...
    "Networks": {
        "network1": {
            ...
        }
    }
}
```

### Data Service

- [Example](data_service_example.png)

## Review and Next Steps

###  Next Steps

- Review Docker documentatin on [Docker Compose](https://docs.docker.com/)
- Containerize more applications
- Create custom repositories
- Docker Swarm
- Kubernetes
- CI/CD
- Mapping to host GPU hardware
