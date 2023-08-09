pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImageName = "my-build-image"
                    def dockerImageTag = "latest"

                    docker.build("${dockerImageName}:${dockerImageTag}", "-f Dockerfile .")
                }
            }
        }
        
        stage('Push to Docker Registry') {
            steps {
                script {
                    def dockerImageName = "my-build-image"
                    def dockerImageTag = "latest"
                    def dockerRegistryUrl = "your-docker-registry-url"
                    
                    docker.withRegistry("https://${dockerRegistryUrl}", 'docker-credentials-id') {
                        dockerImage.push("${dockerImageName}:${dockerImageTag}")
                    }
                }
            }
        }
        
        stage('Run Docker Image') {
            steps {
                script {
                    def dockerImageName = "my-build-image"
                    def dockerImageTag = "latest"
                    
                    docker.image("${dockerImageName}:${dockerImageTag}").run("-p 8080:80")
                }
            }
        }
    }
}
