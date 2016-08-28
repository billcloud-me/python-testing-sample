node ('master'){
    stage 'Checkout'
        checkout scm

    stage 'Prepare Environment'
        sh '''
            #!/bin/bash
            virtualenv venv
            source venv/bin/activate
            pip install -r requirements.txt
        '''
}
