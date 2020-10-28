void setBuildStatus(String message, String state , String scm) {
  step([
      $class: "GitHubCommitStatusSetter",
      reposSource: [$class: "ManuallyEnteredRepositorySource", url: scm],
      contextSource: [$class: "ManuallyEnteredCommitContextSource", context: "ci/jenkins/build-status"],
      errorHandlers: [[$class: "ChangingBuildStatusErrorHandler", result: "UNSTABLE"]],
      statusResultSource: [ $class: "ConditionalStatusResultSource", results: [[$class: "AnyBuildResult", message: message, state: state]] ]
  ]);
}

node {
  stage ("Code Pickup") {
  checkout scm
  }
  
  stage ("Build") {
//    githubNotify status: "PENDING", credentialsId: "my-credentials-id", account: "my-account", repo: "my-repo"
    sh "python3 python.py"
    echo "The build Stage completed Successfully"
  }
  
  stage ("Publish") {
    echo "The Publish Stage completed Successfully"
  }
  
  stage ("Cleanup") {
    echo "The Cleanup Stage completed Successfully"
    sleep 10
    echo "exiting the loop now"
  }
  post {
    success {
            setBuildStatus("Build succeeded", "SUCCESS");
    }
    failure {
            setBuildStatus("Build failed", "FAILURE");
    }
  }
}
