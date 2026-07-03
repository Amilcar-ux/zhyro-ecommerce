pipeline {
    agent any

    tools {
        allure 'Allure_Commandline'
    }

    stages {
        stage('1. Clonar Codigo') {
            steps {
                checkout scm
            }
        }

        stage('2. Preparar Entorno') {
            steps {
                bat '''
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('3. Ejecutar Selenium') {
            steps {
                bat '''
                call venv\\Scripts\\activate
                pytest --alluredir=allure-results
                '''
            }
        }
    }

    post {
        always {
            allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
        }
    }
}
