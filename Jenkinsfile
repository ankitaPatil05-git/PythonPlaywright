pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/ankitaPatil05-git/PythonPlaywright.git', branch: 'master'
            }
        }


        stage('Run Tests') {
            steps {
                bat '''
                pytest --browser_instance=chrome --tracing=on --html=report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'report.html', fingerprint: true
        }
    }
}
