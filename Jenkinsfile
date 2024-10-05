pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Build'
        git branch: 'main', credentialsId: '448df686-fbb8-4108-bd3a-43231ea9ea06', url: 'https://github.com/farheen0204/APITesting.git'
      }
    }

    stage('Test') {
      steps {
        echo 'Test'
        pytest -v
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy'
      }
    }

  }
}
