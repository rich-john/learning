# Use an official Node.js runtime as a parent image
FROM node

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
# Not required, as WORKDIR already sets the context to /app, 
# but it's good practice to be explici
COPY . /app

# Install any needed packages specified in package.json
RUN npm install 

# Make port 80 available to the world outside this container
# Not required, ports published at runtime with -p flag, but it's good practice to document the intended port
EXPOSE 80

# Commands to run the application
CMD ["node", "server.js"]

# then use docker build -t <tag> <path_to_Dockerfile> to build the image