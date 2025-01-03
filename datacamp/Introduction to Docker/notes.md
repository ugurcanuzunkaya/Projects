# Introduction to Docker - Datacamp

## Running Docker Containers

### Presequisites

| Command | Usage |
|---------|-------|
| `nano <filename>` | Open a file in nano text editor |
| `touch <filename>` | Create a new empty file with the specified name |
| `echo <text>` | Print the text to the terminal |
| `<command> >> <filename>` | Append the output of the command to the end of file |
| `<command> -y` | Skip the confirmation prompt and say yes to all |

### Docker CLI

- Docker command line interface will send instructions to the Docker daemon to execute.
- Every command starts with `docker` keyword.

### Docker Container Output

- `docker run <image>` will start a new container from the specified image.
- `docker run hello-world` will run a container that prints a message and exits.
- `docker run ubuntu` will run a container and shut down immediately.
- Adding `-it` flag will keep the container running and open an interactive terminal.
- `docker run -it <image>` will run a container and keep it running.
- `docker run -it ubuntu` will run an ubuntu container and keep it running.
- Adding `-d` to `docker run` will run the container in the background, giving us back control of the shell.
- `docker run -d <image>` will run a container in the background.
- `docker run -d postgres` will run a postgres container in the background.
- `docker ps` will list all the running containers.
- `docker stop <container_id>` will stop the specified container.
- `docker stop <container_name>` will stop the specified container.
- `docker ps -a` will list all the containers, including the stopped ones.

### Summary

| Command | Usage |
|---------|-------|
| `docker run <image>` | Run a container from the specified image |
| `docker run -it <image>` | Run a container and keep it running |
| `docker run -d <image>` | Run a container in the background (detached) |
| `docker ps` | List all the running containers |
| `docker stop <container_id>` | Stop the specified container |

## Working with Docker Containers

### Listing Containers

- `docker run --name <container_name> <image>` will run a container with the specified name.
- `docker ps` will list all the running containers.
- `docker stop <container_name>` will stop the specified container.
- `docker ps -f "name=<container_name>"` will list the specified container. Filter flag `-f` is used to filter the output.
- `docker logs <container_name>` will show the logs of the specified container.
- `docker logs -f <container_name>` will show the logs of the specified container and keep following the logs.
- `docker container rm <container_name>` will remove the specified container. Cleaning up the container is important to avoid cluttering the system.

### Summary of the Last Lesson 1

| Command | Usage |
|---------|-------|
| `docker run --name <container_name> <image>` | Run a container with the specified name |
| `docker ps -f "name=<container_name>"` | List the specified container |
| `docker logs <container_name>` | Show the logs of the specified container |
| `docker logs -f <container_name>` | Show the logs of the specified container and keep following the logs |
| CTRL + C | Stop following the logs |
| `docker container rm <container_name>` | Remove the specified container |

## Managing Local Docker Images

### Docker Hub

- Docker Hub is a cloud-based registry service that allows you to link to code repositories, build your images, test them, and store the images.
- Docker Hub is the default registry where you can find official images.
- `docker pull <image>` will download the specified image from the Docker Hub.
- `docker pull ubuntu` will download the ubuntu image from the Docker Hub.
- `docker pull <image>:<image-version>` will download the specified version of the image.
- `docker pull ubuntu:18.04` will download the ubuntu image with version 18.04.
- `docker pull <image>:<tag>` will download the image with the specified tag.
- `docker images` will list all the images available on the local machine.
- `docker image rm <image>` will remove the specified image from the local machine.
- `docker container prune` will remove all the stopped containers.
- `docker image prune -a` will remove all the images that are not being used by any container.
- Dangling images are the images that have no longer has a name because the name has been re-used for another image. This frequently happens when creating our own images.

### Summary of the Last Lesson 2

| Command | Usage |
|---------|-------|
| `docker pull <image>` | Download the specified image from the Docker Hub |
| `docker pull <image>:<image-version>` | Download the specified version of the image |
| `docker pull <image>:<tag>` | Download the image with the specified tag |
| `docker images` | List all the images available on the local machine |
| `docker image rm <image>` | Remove the specified image from the local machine |
| `docker container prune` | Remove all the stopped containers |
| `docker image prune -a` | Remove all the images that are not being used by any container |

## Distributing Docker Images

### Private Docker Registries

- Unlike Docker official images there is no quality guarantee. There is no security guarantee and working guarantee.
- Name starts with the url of the private registry.
- `docker pull <registry_url>/<image>:<tag>` will download the specified image from the private registry.
- `docker image push <image>` will push the specified image to the Docker Hub.
- Pushing to a specific registry --> name of the image needs to start with the url of the registry.
- `docker image tag <image> <registry_url>/<image>:<tag>` will tag the specified image with the registry url.
- `docker image push <registry_url>/<image>:<tag>` will push the specified image to the private registry.

### Authenticating Against a Registry

- Docker official images --> No need to authenticate.
- Private registries --> Owner can choose
- The standard way to authenticate is to use the `docker login` command.
- `docker login <registry_url>` will authenticate against the specified registry.

### Docker Images as Files

- Sending a Docker image to someone is like sending a file.
- `docker save -o <filename>.tar <image>` will save the specified image to a tar file.
- `docker load -i <filename>.tar` will load the specified image from the tar file.

### Summary of the Last Lesson 3

| Command | Usage |
|---------|-------|
| `docker pull <registry_url>/<image>:<tag>` | Download the specified image from the private registry |
| `docker tag <old-name> <new-name>` | Tag the specified image with the new name |
| `docker image push <registry_url>/<image>:<tag>` | Push the specified image to the private registry |
| `docker login <registry_url>` | Authenticate against the specified registry |
| `docker save -o <filename>.tar <image>` | Save the specified image to a tar file |
| `docker load -i <filename>.tar` | Load the specified image from the tar file |

## Creating Your Own Docker Images

### Creating Images with Dockerfiles

- A Dockerfile is a text file containing all the commands we would run in the command line to install the software we need, with the addition of some Docker-specific syntax.
- [Dockerfile reference](dockerfile.png)
- It should be named `Dockerfile` with no extension to find easily.

### Starting a Dockerfile

- A Dockerfile always start from another image, specified using the `FROM` keyword.
- `FROM <image>` will start the Dockerfile from the specified image.
- `FROM <image>:<tag>` will start the Dockerfile from the specified image with the tag.

### Building a Dockerfile

- `docker build .` will build the Dockerfile in the current directory.
- `docker build /location/to/dockerfile` will build the Dockerfile in the specified location.
- `docker build -t <image-name> .` will build the Dockerfile in the current directory and tag the image with the specified name.
- `docker build -t <image-name>:<tag> .` will build the Dockerfile in the current directory and tag the image with the specified name and tag.

### Customizing Images

- `RUN` keyword is used to run commands in the Dockerfile.
- `RUN <command>` will run the specified command in the Dockerfile.
- `RUN apt-get update` will update the package list in the Dockerfile.
- `RUN apt-get install -y <package>` will install the specified package in the Dockerfile.
- `RUN apt-get install -y python3` will install python3 in the Dockerfile.

### Buildibng a Non-Trivial Dockerfile

- When building an image Docker actually runs commands after RUN
- Docker running `RUN apt-get update` takes the same amount of time as us running it in the terminal.

### Summary of the Last Lesson 4

| Dockerfile Command | Usage |
|--------------------|-------|
| `FROM <image>` | Start the Dockerfile from the specified image |
| `FROM <image>:<tag>` | Start the Dockerfile from the specified image with the tag |
| `RUN <command>` | Run the specified command in the Dockerfile |
| `RUN apt-get install -y <package>` | Install the specified package in the Dockerfile with no confirmation prompt |

| Shell Command | Usage |
|---------------|-------|
| `docker build .` | Build the Dockerfile in the current directory |
| `docker build /location/to/dockerfile` | Build the Dockerfile in the specified location |
| `docker build -t <image-name> .` | Build the Dockerfile in the current directory and tag the image with the specified name |
| `docker build -t <image-name>:<tag> .` | Build the Dockerfile in the current directory and tag the image with the specified name and tag |

## Managing Files in Your Docker Image

### Copying Files into the Image

- The COPY instruction copies files from our local machine into the image we're building.
- `COPY <source> <destination>` will copy the file from the source to the destination.
- If the destination path does not have a filename, the original filename is used:
- `COPY /path/to/file /path/` will copy the file to the destination with the same name.
- Not specifying a filename in the src-path will copy all the file contents.
- `COPY ./<filename>/ /path/` will copy all the files to the destination.
- It is not possible to copy files from a parent directory when building a Dockerfile.

### Downloading Files

- Files are often downloaded from the internet and copied into the image.
- There is an instruction that allows us to do this, the `ADD` instruction.
- `RUN curl <file-url> -o <destination>` will download the file from the url and save it to the destination.
- Example: `RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip`
- `RUN unzip <destination-folder>/<filename>.zip` will unzip the specified file in the destination folder.
- Example: `RUN unzip /pipeline_final.zip`
- `RUN rm <destination-folder>/<filename>.zip` will remove the specified file from the destination folder.
- Example: `RUN rm /pipeline_final.zip`
- Each instruction that downloads files adds to the total size of the image.
- Even if the files are later deleted.
- The solution is to download, unpack and remove files in a single instruction.
- `RUN curl <file-url> -o <destination> \ && unzip <destination-folder>/<filename>.zip \ && rm <destination-folder>/<filename>.zip` will download, unpack and remove the file in a single instruction.

### Summary of the Last Lesson 5

| Dockerfile Command | Usage |
|--------------------|-------|
| `COPY <source> <destination>` | Copy the file from the source to the destination |
| `COPY /path/to/ /path/` | Copy all the files to the destination |
| ~~`COPY ../<file-in-parent-directory>`~~ | We cannot copy files from a parent directory |
| `RUN curl <file-url> -o <destination> \ && unzip <destination-folder>/<filename>.zip \ && rm <destination-folder>/<filename>.zip` | Download, unpack and remove the file in a single instruction |

## Choosing a Start Command for Your Docker Image

### Start Command

- The `CMD` instruction specifies the command that will run when the container starts.
- `CMD <command>` will run the specified command when the container starts.
- The CMD instruction:
  - Runs when the image is started.
  - Does not increase the size of the image.
  - Does not add any time to the build process.
  - If multiple CMD instructions are given, only the last one will run.

### Typical Usage

- Starting an application to run a workflow or that accepts outside connections.
- `CMD python3 my_script.py` will run the python script when the container starts.
- Starting a script that, in turn, starts the multiple application.
- `CMD start.sh` will run the start script when the container starts.

### Stop

- A more general image needs a more general CMD instruction.

### Overriding the default CMD

- `docker run <image> <command>` will override the default CMD instruction.
- `docker run -it <image> <command>` will override the default CMD instruction and keep the container running.
- `docker run -d <image> <command>` will override the default CMD instruction and run the container in the background.
- Example: `docker run -it ubuntu bash` will override the default CMD instruction and open an interactive terminal.

### Summary of the Last Lesson 6

| Dockerfile Command | Usage |
|--------------------|-------|
| `CMD <command>` | Run the specified command when the container starts |

| Shell Command | Usage |
|---------------|-------|
| `docker run <image> <command>` | Override the default CMD instruction |
| `docker run -it <image> <command>` | Override the default CMD instruction and keep the container running |
| `docker run -d <image> <command>` | Override the default CMD instruction and run the container in the background |

## Introduction to Docker Caching

### Docker Build

- RUN instruction that building images can be slow because it runs every shell command in the Dockerfile when building the image.
- This is necessary because what is saved in the resulting image is not the instructions in the Dockerfile but the changes in the filesystem the instructions make during the build process.
- We can view an image as a list of consecutive changes to the filesystem.

### Docker Layers

- Docker layer: All changes made by a single instruction in the Dockerfile.
- Docker image: A list of all the layers. All changes made by all the instructions in the Dockerfile.
- When building an image, Docker checks if the layer has already been built. Tells us the layer is building.

### Docker Caching

- Consecutive builds of the same Dockerfile will be faster because Docker will use the cached layers.
- Docker will only rebuild the layers that have changed.
- Example: `RUN apt-get update` will not be run again if the layer has already been built.

### Understanding the Docker Caching

- When layers are cached helps us understand why sometimes images don't change after a rebuild.
- Docker can't knwo when a new version of a package is available.
- Docker will use cached layers because the instructions are the same.
- Helps us write Dockerfiles that build faster because not all layers need to be rebuilt.
- We order the instructions in the Dockerfile so that the layers that change the least are at the top and most at the bottom.

## Changing Users and Working Directory

### Dockerfile Instruction Interaction

- FROM, RUN, and COPY interact through the filesystem. They influence the filesystem not each other.
- WORKDIR and USER instructions influence the environment of the container. They will influence the other instructions.
- WORKDIR: Changes the working directory of the container.
- USER: Changes the user that runs the instructions in the Dockerfile.

### WORKDIR

- Starting all paths at the root of the filesystem can be cumbersome.
- WORKDIR instruction changes the working directory of the container.
- `WORKDIR /path/to/directory` will change the working directory to the specified path.
- We can work easily with relative paths.
- It affects the following instructions in the Dockerfile.
- Example:
  - `WORKDIR /app`
  - `COPY . .`
  - `RUN python3 my_script.py`
- Example:
  - Before: `CMD /home/repl/projects/pipeline/start.sh`
  - After: `WORKDIR /home/repl/projects/pipeline` \ `CMD start.sh` and we can override the CMD instruction in shell with `docker run <image> start.sh`.

### Linux Permissions

- Permissions are assigned to users.
- The user that runs the instructions in the Dockerfile is root.
- Root has all the permissions.
- Best practice: Use root to create new users with permissions for specific tasks. Then switch to that user and stop using root.

### Changing Users in an Image

- Best practive: Don't run everything as root.
- It is unsafe to run everything as root.
- USER instruction changes the user that runs the instructions in the Dockerfile.
- `USER <username>` will change the user to the specified user.
- The last USER instruction in the Dockerfile will be the user that runs the CMD instruction.
- Example:
  - `USER repl` \ `CMD start.sh` will run the start.sh script as the repl user.

### Summary of the Last Lesson 7

| Dockerfile Command | Usage |
|--------------------|-------|
| `WORKDIR /path/to/directory` | Change the working directory of the container |
| `USER <username>` | Change the user that runs the instructions in the Dockerfile |

## Variables in Dockerfiles

### ARG Instruction

- Create variables in the Dockerfile.
- ARG instruction creates variables that can be passed at build time.
- `ARG <variable>` will create a variable in the Dockerfile.
- `ARG <variable>=<default-value>` will create a variable with a default value.
- Example:
  - `ARG user=app` \ `USER $user` will create a user variable with the default value app and change the user to the app user.
- Example:
  - `ARG path=/home/repl` \ `WORKDIR $path` will create a path variable with the default value /home/repl and change the working directory to /home/repl.
- The variable won't be accessible after the build process. It is only available during the build process.

### Use Cases

- Setting the Python version in the Dockerfile.
- Example:
  - `ARG python_version=3.8` \ `RUN apt-get install -y python$python_version` will set the python version to 3.8 and install python3.8.
- Configuring a folder
- Example:
  - `ARG folder=/app` \ `COPY . $folder` will set the folder to /app and copy all the files to /app.

### Setting ARG variables at build time

- `docker build --build-arg <variable>=<value> .` will set the variable to the specified value at build time.
- Example:
  - Not using docker build:
    - `ARG user=app` \ `USER $user`
  - Using docker build:
    - `docker build --build-arg user=repl .` will set the user variable to repl at build time.
    - `USER $user` will change the user to the repl user.

### Variables with ENV

- ENV instruction creates environment variables that are available during the build process and when the container is running.
- `ENV <variable>=<value>` will create an environment variable with the specified value.
- Example:
  - `ENV user=repl` \ `USER $user` will create an environment variable user with the value repl and change the user to the repl user.

### Use Cases for ENV

- Setting a directory tı be used at runtime.
- Example:
  - `ENV folder=/app` \ `WORKDIR $folder` will create an environment variable folder with the value /app and change the working directory to /app.
- Setting an application to production or development mode.
- Example:
  - `ENV mode=production` \ `CMD python3 my_script.py --mode $mode` will create an environment variable mode with the value production and run the python script in production mode.
- Unlike ARG variables, it is not possible to override ENV variables at build time. However, it is possible to override them at runtime.
- Setting or replacing a variable at runtime
- `docker run --env <variable>=<value> <image>` will set the environment variable to the specified value at runtime.
- Secrets in variables are not secure. They can be accessed by anyone who has access to the image.
- `docker history <image>` will show the history of the image. Also when we pass variables at build or runtime, they will be shown in the history.
- We need to be careful about the variables we pass at build time. We should not pass sensitive information. We need more secure ways to pass sensitive information.

### Summary of the Last Lesson 8

| Dockerfile Command | Usage |
|--------------------|-------|
| `ARG <variable>` | Create a variable in the Dockerfile |
| `ARG <variable>=<default-value>` | Create a variable with a default value |
| `ENV <variable>=<value>` | Create an environment variable with the specified value |

| Shell Command | Usage |
|---------------|-------|
| `docker build --build-arg <variable>=<value> .` | Set the variable to the specified value at build time |
| `docker run --env <variable>=<value> <image>` | Set the environment variable to the specified value at runtime |
| `docker history <image>` | Show the history of the image |

## Creating Secure Docker Images

### Inherent Security

- Docker inherently provides more security than running applications on the host machine. It isolates the application from the host machine.
- However, it is not completely secure. It is possible to break out of the container and access the host machine.
- [Docker security](docker_security.png)

### Making Secure Images

- Attackers can exploit vulnerabilities in the image and break out of the container.
- Additonal security measures are needed to make the images secure to lower the risk of an attack.
- Becomes especially important once exposing the container to the internet.
- It is critical to follow safety measures to protect the container and the host machine when it is in production.

### Images from a Trusted Source

- Creating secure images starts with using images from a trusted source.
- Docker Hub is the default registry where you can find official images. You can easily filter the images by the official tag.
- Keep the images up to date. Docker Hub will show the last update date of the image.
- Keep images minimal. Remove unnecessary packages and files from the image. Install only the packages that are needed.
- Don't run everything as root. Create a new user with the necessary permissions and switch to that user.

## Dockerfile Instructions in the This Folder

- You can easily build my sample Dockerfile with the following commands:

```bash
docker build -t <image-name> .
docker run -it <image-name>
```

- You will get Hello World! message.
- You can give any name or use the below commands.

```bash
docker build -t hello-world-test .
docker run -it hello-world-test
```
