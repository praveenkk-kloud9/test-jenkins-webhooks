node {
  stage ("Build") {
    sh "python3 python.py"
    echo "The build Stage completed Successfully"
  }
  
  stage ("Publish") {
    echo "The Publish Stage completed Successfully"
  }
  
  stage ("Cleanup") {
    echo "The Cleanup Stage completed Successfully"
    sleep 30
    echo "exiting the loop now"
  }
}
