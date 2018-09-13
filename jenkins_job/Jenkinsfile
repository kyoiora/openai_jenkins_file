Jenkinsfile (Declarative Pipeline)
pipeline{
    node('build1'){  
        dir('/root/tengine'){
            sh "pwd"
    
            stage('Git Pull'){
            
                sh '''#!/bin/bash
                        git pull
                '''
              
            }
            stage('Make'){
            
                sh '''#!/bin/bash
                        make -j4
                '''
              
            }
            stage('Make example'){
            
                sh '''#!/bin/bash
                       cd examples/build && make -j4
                '''
              
            }
            stage(' Run SqueezeNet'){
            
                sh '''#!/bin/bash
                        ./build/tests/bin/bench_sqz -r1
                '''
            }
            
            stage(' Run bench_mobilenet'){
            
                sh '''#!/bin/bash
                        ./build/tests/bin/bench_mobilenet -r1
                '''
            }
            stage(' Run Jenkins/test'){
            
                sh '''#!/bin/bash
                        pytest jenkins/test.py  --html=report/test.html --verbose
                '''
    
            }
            post('Publish test results') {
                always{
                    junit allowEmptyResults: true, keepLongStdio: true, testResults: '/root/tengine/report/test.xml'
                }
            } 
            post('Publish HTML results') {
                always{
                    publishHTML([allowMissing: false, alwaysLinkToLastBuild: false, keepAll: false, reportDir: '/root/tengine/report/', reportFiles: 'test.html', reportName: 'HTML Report', reportTitles: ''])
                }
            }       
            
            
        }
    }
}