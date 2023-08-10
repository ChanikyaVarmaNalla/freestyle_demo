pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_CREDENTIALS = credentials('c22e28f9-2cda-4794-9907-79ecefbbb0ab')
        DOCKER_IMAGE_NAME = 'my-docker-build-image'
        CONTAINER_NAME = 'my-docker-container'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE_NAME, '-f Dockerfile .')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://hub.docker.com', DOCKER_REGISTRY_CREDENTIALS) {
                        docker.image(DOCKER_IMAGE_NAME).push()
                    }
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    def myContainer = docker.image(DOCKER_IMAGE_NAME).container(CONTAINER_NAME)
                    myContainer.start("-d")
                }
            }
        }
    }

    post {
        always {
            script {
                try {
                    def myContainer = docker.image(DOCKER_IMAGE_NAME).container(CONTAINER_NAME)
                    myContainer.stop()
                } catch (Exception e) {
                    echo "Error stopping container: ${e}"
                }
            }
        }
    }
}
