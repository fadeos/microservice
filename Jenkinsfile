stage 'Build-testing'
node("master") {
   echo 'Build a testing evn for new build'
   dir('.') {
    // run build file
    sh 'sh ./test-build.sh'
}
}
