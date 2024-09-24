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
            steps {
                sh "echo Test stage"
            }
        }
        stage('Delivery') {
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: 'user_01',
                        passwordVariable: 'gitPassword',
                        usernameVariable: 'gitUsername',
                    )]
                ){
                    sh "echo ${gitPassword} ${gitUsername}"
                }
            }
        }
    }
}