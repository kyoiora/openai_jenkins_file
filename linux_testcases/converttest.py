
                    rm -rf models/*.tmfile
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/sqz.prototxt -m models/squeezenet_v1.1.caffemodel -o models/squeezenet.tmfile

             print 'Create mobilenet'
             sh '''#!/bin/bash
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/mobilenet_deploy.prototxt -m models/mobilenet.caffemodel -o models/mobilenet.tmfile

            '''
             print 'Create resnet50'
             sh '''#!/bin/bash
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/resnet50.prototxt -m models/resnet50.caffemodel -o models/resnet50.tmfile

            '''
             print 'Create googlenet'
             sh '''#!/bin/bash
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/googlenet.prototxt -m models/googlenet.caffemodel -o models/googlenet.tmfile

            '''
             print 'Create inception_v4'
             sh '''#!/bin/bash
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/inception_v4.prototxt -m models/inception_v4.caffemodel -o models/inception_v4.tmfile

             '''
             print 'Create inception_v3'
             sh '''#!/bin/bash
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/deploy_inceptionV3.prototxt -m models/deploy_inceptionV3.caffemodel -o models/inception_v3.tmfile

            '''
             print 'Create alexnet'
             sh '''#!/bin/bash
                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/alex_deploy.prototxt -m models/alexnet.caffemodel -o models/alexnet.tmfile

            '''
             print 'Create vgg16'
             sh '''#!/bin/bash
#                    ./build/tools/bin/convert_model_to_tm -f caffe -p models/vgg16.prototxt -m models/vgg16.caffemodel -o models/vgg16.tmfile

            '''

        }

stage(' Run Convate'){
                    sh '''#!/bin/bash
                    make install
                    cd examples/tengine_model/classification
                    cmake -DTENGINE_DIR=/home/rk/tengine .
                    make

                    '''
                    print 'Run squeezenet'
                    sh '''#!/bin/bash
                           ./examples/tengine_model/classification/tm_classify -n squeezenet
                    '''
                     print 'Run mobilenet'
                     sh '''#!/bin/bash
                            ./examples/tengine_model/classification/tm_classify -n mobilenet

                    '''
                     print 'Run resnet50'
                     sh '''#!/bin/bash
                            ./examples/tengine_model/classification/tm_classify -n mobilenet

                    '''
                     print 'Run googlenet'
                     sh '''#!/bin/bash
                            ./examples/tengine_model/classification/tm_classify -n googlenet

                    '''
                     print 'Run inception_v4'
                     sh '''#!/bin/bash
                            ./examples/tengine_model/classification/tm_classify -n inception_v4

                     '''
                     print 'Run inception_v3'
                     sh '''#!/bin/bash
                            ./examples/tengine_model/classification/tm_classify -n inception_v3
                    '''
                     print 'Run alexnet'
                     sh '''#!/bin/bash
                            ./examples/tengine_model/classification/tm_classify -n alexnet

                    '''
                     print 'Run vgg16'
                     sh '''#!/bin/bash
        #                   ./examples/tengine_model/classification/tm_classify -n vgg16 -i tests/images/bike.jpg

                    '''

                }