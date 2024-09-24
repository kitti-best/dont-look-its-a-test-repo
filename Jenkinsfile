pipeline {
    agent {vm2}
    environment {
        APP_NAME = "test app name"
    }
    stages {
        stage('Build Image') {
            steps {
                sh "ls"
                sh "echo ${env.APP_NAME}"
            }
        }
    }
}