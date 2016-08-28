node ('master'){
    stage 'Checkout'
        checkout scm

    stage 'Prepare Environment'
        deleteDir()
        sh '''
            #!/bin/bash
            virtualenv venv
            . venv/bin/activate
            pip install -r requirements.txt
        '''
}
