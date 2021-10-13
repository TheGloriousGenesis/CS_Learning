`# Docker

## Why Docker?
Docker was created to solve installation problems on any computer. This means one does not have to worry about setup or program dependencies when install programs

## Glossary
| Term|Definition|
|:---:|:--------:|
|Namescaping (Linux)|Portioning a section of the hard drive for certain process/es|
|Control Group (Linux) | Determining how much resources is used for a given process|
|Docker image| A file system snapshot|
|Docker CLI| A client that communicates commands to Docker server|
|Docker Server| A server that is in charge of creating images and containers|
|Container| Specific grouping of resources. ![image info](./Container.png) |
| Kernel | A kernel is communicator level between processes (like programs) and hardware (CPU/DISK)|

## What is Docker?
- Ecosystem that runs container

## How does Docker work?

- When you run a docker command (send command to Docker CLI, processes then send to server), it communicates with the Docker Hub and tells it to download an image
  (which is a file of dependancies and instructions to create a specific progam). This image is then downloaded onto local
pc. This image can be used to create the program it describes in a Docker container (which is an instance of the image, and a running version of the image program)
- When an image is created, it is composed of two things: *FS Snapshot* and *Startup Command*. When a container is created,
it takes the *FS Snapshot* and sections away a portion of the hard drive for the programs/processes needed (installs them). It then runs the startup
command, which starts the running of a new instance the programs/processes.

### Containers
- Create container `docker create <image>` and starting container `docker start <container id>` is different!
- `docker run` (shows logs from terminal as default) and `docker start` (doesn't show logs as default)
- When container exited, it can be run again by `docker start` command
- Can not overwrite default command if container is running with a command already.
- To stop a container can use `docker stop` or `docker kill`
  - `docker stop` gives system call `SIGTERM` which allows system some time before stopping the main process in the container. Good if clean up needed before process has stopped
  - `docker kill` gives system call `SIGKILL`, doesn't give any time. Terminates container immediately
  - If `docker stop` doesn't work within 10 seconds, automatic trigger of `docker kill` is executed.
  - Preferred: `docker stop`
- To execute many processes within the container other than primary, use `docker exec -it <container-id> <command>`. The
`-it` parameter allows interaction with the container through terminal


## Useful Commands
|Command|Description|
|:-----:|:---------:|
|`docker system prune`| Removes all stopped containers on disk|
|`docker stop`| Stops container running process|
|`docker exec -it <container-id> <command>`|Run another process in container|
