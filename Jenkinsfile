/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'mcr.microsoft.com/playwright:v1.34.0-jammy' } }
    stages {
        stage(‘test’) {
            steps {
                sh 'pytest -m regression Case1’ 
            }
        }
    }
}