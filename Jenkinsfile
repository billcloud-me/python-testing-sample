node ('master'){
    stage 'Checkout'
        checkout scm

    stage 'Prepare Environment'
        sh '''
            #!/bin/bash
            virtualenv venv
            . venv/bin/activate
            pip install -r requirements.txt
        '''

    stage 'Clean Up'
        deleteDir()
}
