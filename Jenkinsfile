pipeline {
    agent any

    stages {
        stage('clone the code') {
            steps {
                echo "clone code"
                git url:"https://github.com/vinaykumarb2424/Alphabin.git", branch: "main"
            }
        }
        stage('build') {
            steps {
                echo "building docker image"
                bat "docker build -t docker1 ."
            }
        }
        stage('push image to docker hub') {
            steps {
                echo "pushing image to docker hub"
                withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'dockerpassword', usernameVariable: 'dockerusername')]) {
                //echo "${dockerusername} ${dockerpassword}"
                bat "docker tag docker1 ${dockerusername}/docker1:latest"
                bat "docker login -u ${dockerusername} -p ${dockerpassword}"
                bat "docker push  ${dockerusername}/docker1:latest"


                }
            }
        }
        stage('deploy') {
            steps {
                echo "deploying container"
                bat "docker run -d --rm --name docker1-container docker1"
                echo "deployed successfully"
            }
        }
    }
}
a