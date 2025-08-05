pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'simple-python-app'
        DOCKER_TAG = "${env.BUILD_ID}"
        CONTAINER_NAME = 'python-app-container'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', 
                url: 'https://github.com/Akhil-7777/Project',
                credentialsId: 'your-github-credentials' // If private repo
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install pytest==7.4.0'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "Current directory structure:"
                ls -lR
                python3 -m pytest ./tests/ -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}:${DOCKER_TAG}")
                }
            }
        }

        stage('Deploy to Docker') {
            steps {
                script {
                    // Stop and remove any existing container
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    
                    // Run new container
                    sh """
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        -p 5000:5000 \
                        ${DOCKER_IMAGE}:${DOCKER_TAG}
                    """
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed'
            cleanWs() // Clean workspace
        }
        success {
            echo 'Deployment succeeded!'
            slackSend(color: 'good', message: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'")
        }
        failure {
            echo 'Deployment failed!'
            slackSend(color: 'danger', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'")
        }
    }
}
