void setBuildStatus(String message, String state , String scm) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: scmRepo],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

node {
  try {
  stage ("Code Pickup") {
  checkout scm
  setBuildStatus("Code Pickup Succeeded", "SUCCESS",scm); 
  }
  } catch(e) {
    setBuildStatus(e, "FAILURE",scm); 
    throw e
  }
  
  try {
  stage ("Build") {
    sh "python3 python.py"
    echo "The build Stage completed Successfully"
  }
  setBuildStatus("Code Build Succeeded", "SUCCESS",scm); 
  }catch(e) {
    setBuildStatus(e, "FAILURE",scm); 
    throw e
  }

  try {
  stage ("Publish") {
    echo "The Publish Stage completed Successfully"
  }
  setBuildStatus("Code Publish Succeeded", "SUCCESS",scm); 
  } catch(e) {
   setBuildStatus(e, "FAILURE",scm);
    throw e
  }

  try {
  stage ("Cleanup") {
    echo "The Cleanup Stage completed Successfully"
    sleep 10
    echo "exiting the loop now"
  }
   setBuildStatus("Code Cleanup Succeeded", "SUCCESS",scm);
  } catch(e) {
   setBuildStatus(e, "FAILURE",scm);
    throw e
  }
}
