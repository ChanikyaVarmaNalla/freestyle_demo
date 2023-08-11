pipeline {
    agent any
    environment {
        //once you sign up for Docker hub, use that user_id here
        registry = "chanikyavarmanalla/my-docker-image"
        //- update your credentials ID after creating credentials for connecting to Docker Hub
        registryCredential = '14ae160d-e567-46fc-a107-073fa8e06815'
        dockerImage = ''
    }

    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'git@github.com:ChanikyaVarmaNalla/freestyle_demo.git']]])
            }
        }

    // Building Docker images
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build registry
        }
      }
    }

     // Uploading Docker images into Docker Hub
    stage('Upload Image') {
     steps{
         script {
            docker.withRegistry( '', registryCredential ) {
            dockerImage.push()
            }
        }
      }
    }

    // Running Docker container, make sure port 8096 is opened in
    stage('Docker Run') {
     steps{
         script {
           bat "docker run %registry%"
         }
      }
    }
  }
}