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
                bat 'pip install -r requirements.txt'
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
