/* Requires the Docker Pipeline plugin */
pipeline {
    agent any
    stages {
        stage(‘Test’) {
            steps {
                sh 'docker-compose up’
            }
        }
    }
}