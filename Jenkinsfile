pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_CREDENTIALS = credentials('da0a243d-d4c3-44de-bfed-64a982c8dab5')
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
                    def dockerImage = docker.build(DOCKER_IMAGE_NAME, '-f Dockerfile .')
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://docker.io', DOCKER_REGISTRY_CREDENTIALS) {
                        docker.image(DOCKER_IMAGE_NAME).push()
                    }
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    def myContainer = docker.container().from(docker.image(DOCKER_IMAGE_NAME).run("-d", name: CONTAINER_NAME))
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
                    echo "Container stopped successfully"
                } catch (Exception e) {
                    echo "Error stopping container: ${e}"
                }
            }
        }
    }
}
