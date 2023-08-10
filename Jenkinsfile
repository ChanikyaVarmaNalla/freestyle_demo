pipeline {
    agent any

    environment {
        DOCKER_REGISTRY_CREDENTIALS = credentials('c22e28f9-2cda-4794-9907-79ecefbbb0ab')
        DOCKER_IMAGE_NAME = 'my-docker-build-image'
        GIT_REPO_URL = 'https://github.com/ChanikyaVarmaNalla/freestyle_demo.git'
    }

    stages {
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
                    docker.withRegistry('', DOCKER_REGISTRY_CREDENTIALS) {
                        dockerImage.push()
                    }
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE_NAME).run()
                }
            }
        }
    }

    post {
        always {
            // Clean up by stopping and removing the running container
            script {
                docker.image(DOCKER_IMAGE_NAME).stop()
                docker.image(DOCKER_IMAGE_NAME).remove()
            }
        }
    }
}
