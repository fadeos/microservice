#!/usr/bin/env groovy
node {
  stage("OTA preparation"){
    sh "PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH"
    sh "if [ ! -d 'buildenv' ]; then python3 -m venv buildenv fi"
    sh ". buildenv/bin/activate"
    sh "pip install -r requirements.txt"
  }
  stage("OTA Unit Test"){
    echo 'OK'
  }
  stage("OTA Functional Test"){
    echo 'OK'
  }
  stage("OTA Integration Test"){
    echo 'OK'
  }
  stage("OTA release Approuved"){
    echo 'OK'
  }
}
