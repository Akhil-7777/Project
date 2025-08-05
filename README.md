# Simple Python Application with Docker Deployment

This project demonstrates a simple Python application deployed using Docker and automated with a Jenkins pipeline.

## Project Overview

- A basic Python application containerized with Docker
- Automated CI/CD pipeline using Jenkins
- Testing with pytest
- Deployment to a Docker container

## Prerequisites

- Jenkins server (running on Amazon EC2 in this case)
- Docker installed on the Jenkins server
- Python 3.9+ installed
- GitHub repository access

## Jenkins Pipeline Setup

The Jenkins pipeline performs the following steps:

1. **Checkout Code**: Clones the repository from GitHub
2. **Install Dependencies**: Installs pytest for testing
3. **Run Tests**: Executes unit tests using pytest
4. **Build Docker Image**: Creates a Docker image of the application
5. **Deploy to Docker**: Runs the application in a Docker container

### Jenkinsfile

```groovy
[paste your entire Jenkinsfile content here]
