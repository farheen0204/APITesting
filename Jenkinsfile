pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        echo 'Build'
        git branch: 'main', credentialsId: '448df686-fbb8-4108-bd3a-43231ea9ea06', url: 'https://github.com/farheen0204/APITesting.git'
      }
    }

    stage('Run Test') {
      steps {
        echo 'Test'
        sh 'pip3 install requests'
        sh 'python3 -m pytest -v -s'
      }
    }

    stage('Deploy') {
      steps {
        echo 'Deploy'
      }
    }

  }
}
