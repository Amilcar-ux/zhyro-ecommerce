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
                :: Agregamos la ruta del sistema donde Windows guarda el lanzador 'py'
                SET PATH=%PATH%;C:\\Windows
                
                py -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('3. Ejecutar Selenium') {
            steps {
                bat '''
                :: Aseguramos la ruta también en esta etapa
                SET PATH=%PATH%;C:\\Windows
                
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
