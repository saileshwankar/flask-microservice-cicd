pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/saileshwankar/flask-microservice-cicd.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Use python -m pip instead of pip directly
                bat 'python -m pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                bat 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t flask-microservice:latest .'
            }
        }
    }
}
