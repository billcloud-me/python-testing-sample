node ('master'){
    stage 'Checkout'
        checkout scm

    stage 'Prepare Environment'
        sh 'virtualenv venv'
        sh 'source venv/bin/activate'
        sh 'pip install -r requirements.txt'
}
