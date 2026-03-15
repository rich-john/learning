# Use an official Node.js runtime as a parent image
FROM node

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
# Not required, as WORKDIR already sets the context to /app, 
# but it's good practice to be explici
COPY . /app

#
RUN npm install 

#
EXPOSE 80

# Commands to run the application
CMD ["node", "server.js"]