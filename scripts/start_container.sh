#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull asif9720/python_app

# Run the Docker image as a container
docker run -d -p 5000:5000 asif9720/python_app