pipeline {
    agent any
    environment {
        DOCKER_HUB_USER = 'harivarsan1177'
        IMAGE_NAME = 'menu-calculator'
        REGISTRY_CRED_ID = 'docker-hub-credentials'
    }
    stages {
        stage('Source Code') {
            steps {
                echo 'Source Code Checkout Complete'
            }
        }
        stage('Version Control') {
            steps {
                script {
                    def gitCommit = powershell(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                    env.GIT_COMMIT_SHA = gitCommit
                    echo "Current Commit SHA: ${env.GIT_COMMIT_SHA}"
                }
            }
        }
        stage('Continuous Integration') {
            steps {
                powershell '''
                python -m venv venv
                .\\venv\\Scripts\\pip.exe install -r requirements.txt
                .\\venv\\Scripts\\python.exe -m pytest test_app.py -v
                '''
            }
        }
        stage('Build & Push') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: env.REGISTRY_CRED_ID, passwordVariable: 'DOCKER_REGISTRY_PWD', usernameVariable: 'DOCKER_REGISTRY_USER')]) {
                        powershell "docker build -t ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.GIT_COMMIT_SHA} ."
                        powershell "echo \$env:DOCKER_REGISTRY_PWD | docker login -u \$env:DOCKER_REGISTRY_USER --password-stdin"
                        powershell "docker push ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.GIT_COMMIT_SHA}"
                    }
                }
            }
        }
        stage('Deployment') {
            steps {
                powershell "sed -i 's|IMAGE_PLACEHOLDER|${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.GIT_COMMIT_SHA}|g' deployment.yaml"
                powershell "kubectl apply -f deployment.yaml"
                powershell "kubectl apply -f service.yaml"
            }
        }
    }
}
