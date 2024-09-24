pipeline {
    agent { label 'vm2' }
    environment {
        APP_NAME = "simple api"
    }
    stages {
        stage('Build Image') {
            steps {
                sh "echo ${env.APP_NAME}"
                sh "docker version"
                sh "docker-compose up --build -d"
            }
        }
        stage('Test') {
        
        }
        stage('Delivery') {
            steps {
                withcredentials(
                    [usernamePassword(
                        credentialId: 'user_01',
                        passwordVariable: 'gitPassword',
                        usernameVariable: 'gitUsername',
                    )]
                )
                sh "echo ${gitPassword} ${gitUsername}"
            }
        }
    }
}