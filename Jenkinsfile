pipeline {

    agent any

    stages {

        stage('Build Images') {

            steps {

                sh 'docker build -t mmcgarrigle/service_1 ./Service_1'
                sh 'docker build -t mmcgarrigle/service_2 ./Service_2'
                sh 'docker build -t mmcgarrigle/service_3 ./Service_3'
                sh 'docker build -t mmcgarrigle/service_4 ./Service_4'

            }

        }

    }

}