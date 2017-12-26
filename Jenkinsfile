stage 'Build-testing'
node("master") {
   echo 'Build a testing evn for new build'
   dir('./test-build') {
    // run build file
    sh 'sh ./test-build.sh'
}
}
