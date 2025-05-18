pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/flask-microservice.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Unit Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-microservice:latest .'
            }
        }
    }
}
