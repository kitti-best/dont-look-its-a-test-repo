pipeline {
    agent none
    environment {
        APP_NAME = "simple api"
        IMAGE_NAME = "ghcr.io/kitti-best/sdpx-jenkins-container"
    }
    stages {
        stage("Unit test") {
            agent { label "vm2" }
            steps {
                sh "coverage run -m unittest app/unit_test.py -v"
                sh "coverage report -m"
            }

        }
        stage("Robot test") {
            agent { label "vm2" }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "user_01",
                        passwordVariable: "gitPassword",
                        usernameVariable: "gitUsername",
                    )]
                ){
                    sh "docker login --username ${gitUsername} --password ${gitPassword} ghcr.io"
                    sh "docker build app/ -t ${IMAGE_NAME}"
                    sh "docker run -d -p 8080:5000 ${IMAGE_NAME}"  // HOST:CONTAINER

                    git url: "https://github.com/kitti-best/dont-look-its-test-repo-for-testing-another-repo"
                    sh "robot robot_test.robot"
                    sh "ls"
                    sh "pwd"

                    sh "docker push ${IMAGE_NAME}"
                    sh "docker ps -aq"
                    sh "docker stop \$(docker ps -aq)"
                    sh "docker rm \$(docker ps -aq)"
                    sh "docker rmi \$(docker images -q)"
                }
            }
        }
        stage("Create Docker Container") {
            agent { label "vm3" }
            steps {
                withCredentials(
                    [usernamePassword(
                        credentialsId: "user_01",
                        passwordVariable: "gitPassword",
                        usernameVariable: "gitUsername",
                    )]
                ){
                    sh "docker login --username ${gitUsername} --password ${gitPassword} ghcr.io"
                    sh "docker run -d -p 8080:5000 ${IMAGE_NAME}"  // HOST:CONTAINER
                    // Use ssh -L 80:127.0.0.0.1:8080 kitti@192.168.182.103 to ssh
                }
            }
        }
    }
}