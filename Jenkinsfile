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
                    withDockerRegistry(credentialsId: env.REGISTRY_CRED_ID, url: 'https://docker.io') {
                        powershell "docker build -t ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.GIT_COMMIT_SHA} ."
                        powershell "docker push ${env.DOCKER_HUB_USER}/${env.IMAGE_NAME}:${env.GIT_COMMIT_SHA}"
                    }
                }
            }
        }
        stage('Deployment') {
            steps {
                powershell '''
                (Get-Content deployment.yaml) -replace 'IMAGE_PLACEHOLDER', "$env:DOCKER_HUB_USER/$env:IMAGE_NAME:$env:GIT_COMMIT_SHA" | Set-Content deployment.yaml
                kubectl apply -f deployment.yaml --validate=false
                kubectl apply -f service.yaml --validate=false
                git checkout deployment.yaml
                '''
            }
        }
    }
}
