PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "buildenv" ]; then
        python3 -m venv buildenv
fi

. buildenv/bin/activate
pip install -r requirements.txt
nose2
nose2 --with-coverage --coverage-report=xml
nose2 --plugin nose2.plugins.junitxml --junit-xml
pylint --disable=cyclic-import --rcfile=pylint.cfg -r y flaskr/ > pylint.log;  echo "pylint tests done"


node {
  stage("OTA preparation"){
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
