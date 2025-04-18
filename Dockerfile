# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Add metadata labels
LABEL maintainer="Vipul Singh Parmar <github.com/jhonney13>"
LABEL description="Heart Disease Prediction App for Azure deployment"
LABEL version="1.0"

# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip3 install -r requirements.txt

# Copy the rest of the application
COPY . .

# Run app.py when the container launches
CMD ["python3", "app.py"]