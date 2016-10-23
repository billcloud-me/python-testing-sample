node ('master'){
    stage 'Checkout'
        deleteDir()
        checkout scm

    stage 'Prepare Environment'
        sh '''
            #!/bin/bash
	    alias python=python3
            virtualenv ../venv
            . ../venv/bin/activate
            pip install -r requirements.txt
        '''
    
    stage 'Unit Testing'
        sh '''
            . ../venv/bin/activate
            pytest
        '''

    stage 'Behave Testing'
        sh '''
            . ../venv/bin/activate
            behave
        '''

    stage 'Clean Up'
        deleteDir()
}
