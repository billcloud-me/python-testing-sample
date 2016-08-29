node ('master'){
    stage 'Checkout'
        deleteDir()
        checkout scm

    stage 'Prepare Environment'
        sh '''
            #!/bin/bash
            virtualenv ../venv
            . ../venv/bin/activate
            pip install -r requirements.txt
        '''
    
    stage 'Unit Testing'
        sh '''
            . ../venv/bin/activate
            pytest
        '''

    stage 'Clean Up'
        deleteDir()
}
