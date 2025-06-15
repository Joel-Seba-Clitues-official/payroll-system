pipeline {
    agent any

    environment {
        IMAGE_NAME = 'payroll-app'
        CONTAINER_NAME = 'payroll-container'
        APP_PORT = '5000'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/payroll-system.git' // ← Change this
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any running instance
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"

                    // Run new container
                    sh "docker run -d -p ${APP_PORT}:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "App is running at http://localhost:${APP_PORT}"
        }
        failure {
            echo "Pipeline failed!"
        }
    }
}
