/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'pytest-playwright' } }
    stages {
        stage(‘Test’) {
            steps {
                docker.image("pytest-playwright").run('--env TEST_EMAIL=valid@example.io --env TEST_PASSWORD=valid --volume Case1:Case1:rw')
                sh 'pytest --html=/Case1/result/result.html --self-contained-html -m regression Case1’
            }
        }
    }

    post {
        always {
            // clean up
            script {
                docker.image("pytest-playwright").stop()
                docker.image("pytest-playwright").remove()
            }
        }
    }
}