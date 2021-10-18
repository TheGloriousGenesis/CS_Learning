# Java image

## Details
This is a java image to run a program to add a series of 5 numbers.

## Prerequisites 
- Docker installed

## Run instructions
Run the following commands
- `docker build .`
- Obtain image id
- `docker run -it <image-id>`

## Study details
### Dockerfile
- It is easy to build the .jar file locally and move it but that is a lot of effort from dev view
- Separate into build and package stages by putting `as BUILD` tag. This allows light-weight images. In this case images 
were the same size XD
  - Using separate build and package stage, good if you do not want to have separate services running using maven. 