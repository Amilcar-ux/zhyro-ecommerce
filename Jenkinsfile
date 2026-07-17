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
                SET PATH=%PATH%;C:\\Python313;C:\\Python313\\Scripts
                python -m venv venv
                call venv\\Scripts\\activate
                pip install -r requirements.txt
                '''
            }
        }

        stage('3. Ejecutar Selenium') {
            steps {
                bat '''
                SET PATH=%PATH%;C:\\Python313;C:\\Python313\\Scripts
                call venv\\Scripts\\activate
                
                :: 1. Ejecutamos las pruebas como de costumbre
                pytest --alluredir=allure-results
                
                :: 2. Creamos y llenamos el archivo environment.properties dinámicamente
                echo Browser=Chrome > allure-results\\environment.properties
                echo Browser.Version=126.0 >> allure-results\\environment.properties
                echo Platform=Windows 11 >> allure-results\\environment.properties
                echo Project=DocMeet >> allure-results\\environment.properties
                echo Executor=Jenkins >> allure-results\\environment.properties
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
