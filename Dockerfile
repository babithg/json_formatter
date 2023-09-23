# Use the Python image with Alpine Linux as the base image
FROM python:alpine

# Set the maintainer label
LABEL maintainer="babithg@gmail.com"

# Copy the current directory contents into the container at /app
COPY . /app

# Set the working directory in the container
WORKDIR /app

# Install the required packages
RUN pip install -r requirements.txt

# Application Access port 
EXPOSE 8080

# Define the entry point for the container
ENTRYPOINT ["python"]

# Set the default command to run when the container starts
CMD ["app.py"]