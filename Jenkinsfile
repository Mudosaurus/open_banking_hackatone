pipeline {
    agent any

    stages {
        stage('Clean') {
            steps {
                sh 'docker-compose down  || echo Images not found, continue step'
                sh 'docker image prune -f || echo Not found stopped images'
            }
        }

        stage('Fetch Server') {
            steps {
                git branch: 'master', credentialsId: 'github', url: 'https://github.com/Mudosaurus/open_banking_hackatone.git'
            }
        }

        stage('Fetch Client') {
            steps {
                dir('social') {
                    git branch: 'main', credentialsId: 'p100lab', url: 'https://github.com/Pro100Lab/TheSocialT087.git'
                }
            }
        }

        stage('Build Client') {
            steps {
                dir('social') {
                    sh 'npm install'
                    sh 'npm run build'
                }
            }
        }
        stage('Fetch Config') {
            steps {
                dir('SpaceConfigs') {
                    git branch: 'rc-2.15.001', credentialsId: 'p100lab', url: 'https://github.com/Pro100Lab/SpaceCraftConfigurations.git'
                }
            }
        }
        stage('Build Nginx') {
             steps {
                dir('nginxbuilder') {
                    sh 'rm -rf html'
                    sh 'rm -rf sites-enabled'
                    sh 'mkdir html'
                    sh 'cp -r ../social/dist ./html/public'
                    sh 'cp ../SpaceConfigs/nginx/Nginx.Dockerfile ./Dockerfile'
                    sh 'cp ../SpaceConfigs/nginx/nginx.conf ./nginx.conf'
                    sh 'cp -r ../SpaceConfigs/nginx/sites-enabled ./sites-enabled'
                    sh 'cp -r ../SpaceConfigs/nginx/letsencrypt ./letsencrypt'
                }
            }
        }

        stage('Deploy all') {
            steps {
                sh 'docker-compose up --build --detach && docker start djangos_web_1 || error during starting service'
            }
        }
    }
}