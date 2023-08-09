# Use a base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Install git
RUN apt-get update && apt-get install -y git

# Clone the source code from Git
RUN git clone https://github.com/ChanikyaVarmaNalla/freestyle_demo.git

# Set the working directory to the cloned repo
WORKDIR /app/freestyle_demo

# Install required dependencies from requirements.txt
RUN pip install -r requirements.txt

# Run your script
CMD ["python", "sample.py"]
