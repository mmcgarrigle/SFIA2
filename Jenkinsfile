pipeline {

    agent any

    stages {

         stage('Run Playbook') {

                steps {
                    sh 'chmod +x ./scripts/*.sh'
                    sh './scripts/ansible.sh'
                }
        }

        stage('Build Images') {

            steps {
                sh './scripts/build_images.sh'
            }

        }

        stage('Deploy Stack') {

            steps {
                sh './scripts/deploy_stack.sh'
            }
        }

        stage('Clean') {

            steps {
                sh './scripts/clean.sh'
            }
        }

    }

}