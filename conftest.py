import pytest
import os
import asciitable
import collections
import pdb

android_testlist=['imagenet_sqz','imagenet_alexnet','imagenet_googlenet',
                  'imagenet_mobilenet','imagenet_inception_v3',
                  'imagenet_inception_v4',
                  'imagenet_resnet50','imagenet_vgg16']

RK3399_PT_testlist=['squeezenet_FP32_1xA72','squeezenet_Int8_1xA72','squeezenet_FP32_2xA72','squeezenet_Int8_2xA72',
                    'squeezenet_FP32_1xA53','squeezenet_Int8_1xA53','squeezenet_FP32_4xA53','squeezenet_Int8_4xA53',
                    'mobilenet_FP32_1xA72','mobilenet_Int8_1xA72','mobilenet_FP32_2xA72','mobilenet_Int8_2xA72',
                    'mobilenet_FP32_1xA53','mobilenet_Int8_1xA53','mobilenet_FP32_4xA53','mobilenet_Int8_4xA53','RK3399_testresult',]

RK3288_PT_testlist=['squeezenet_FP32_1xA17','squeezenet_Int8_1xA17','squeezenet_FP32_4xA17','squeezenet_Int8_4xA17',
                    'mobilenet_FP32_1xA17','mobilenet_Int8_1xA17','mobilenet_FP32_4xA17','mobilenet_Int8_4xA17','RK3288_testresult',]

BananaPi_PT_testlist=['squeezenet_FP32_1xA7','squeezenet_Int8_1xA7','squeezenet_FP32_4xA7','squeezenet_Int8_4xA7',
                    'mobilenet_FP32_1xA7','mobilenet_Int8_1xA7','mobilenet_FP32_4xA7','mobilenet_Int8_4xA7','Bananapi_testresult',]

linux_testlist=[  'get_node','imagenet_sqz','imagenet_alexnet','imagenet_googlenet',
                  'imagenet_mobilenet','imagenet_inception_v3',
                  'imagenet_inception_v4','test_tf_mobilenet','test_tf_inceptionv3',
                  'imagenet_resnet50','imagenet_vgg16','ssd','mssd','yolov2','faster_rcnn','mtcnn','lighten_cnn',
                  'caffe_wrapper_sqz','caffe_wrapper_mobilenet','caffe_wrapper_mtcnn_4faces',
                  'caffe_wrapper_mtcnn_6faces','tf_wrapper_inceptionv3','tf_wrapper_mobilenet',
                  'bench_sqz_net','bench_mobile_net','vgg16_mem','Convert_squeezenet','Convert_mobilenet','Convert_resnet50',
                  'Convert_googlenet','Convert_inception_v3','Convert_inception_v4','Convert_alexnet','Convert_vgg16']

def pytest_addoption(parser):
	parser.addoption(
		"--cmdopt", action="store", default="onboard", 
		help="my option: onboard or cc or adb"
	)
	parser.addoption(
		"--targetdir", action="store", default="/root/tengine/", 
		help="dir of target targetdir"
	)
	parser.addoption(
		"--ip", action="store", default="", 
		help="ip of android device"
	)
@pytest.fixture
def cmdopt(request):
	return request.config.getoption("--cmdopt")

@pytest.fixture
def targetdir(request):
	return request.config.getoption("--targetdir")

@pytest.fixture
def ip(request):
	return request.config.getoption("--ip")

def pytest_generate_tests(metafunc):
    print metafunc.config.getoption('cmdopt')
    # if linux test job get parmetrize from core_test.list
    if metafunc.config.getoption('cmdopt') == "linuxFT":
        #if 'testcase_dict' in metafunc.fixturenames:
        #test_path = metafunc.config.getoption('targetdir')
        #testcase_list=collections.OrderedDict()
        #print(test_path)
        #testlist=asciitable.read(test_path+'/jenkins/core_test.list')

        #for rec in testlist:
        #testcase_list[rec[0]]=rec[1]
        #pprint.pprint(dict(testcase_list.items()))
        #metafunc.parametrize("testcase_dict", testcase_list.keys())
        metafunc.parametrize("testcase_dict", linux_testlist)
        print(linux_testlist)
    elif metafunc.config.getoption('cmdopt') == "linuxPT3399":
        metafunc.parametrize("testcase_dict", RK3399_PT_testlist)
    elif metafunc.config.getoption('cmdopt') == "linuxPT3288":
        metafunc.parametrize("testcase_dict", RK3288_PT_testlist)
        print(RK3288_PT_testlist)
    elif metafunc.config.getoption('cmdopt') == "linuxPTBananapi":
        metafunc.parametrize("testcase_dict", BananaPi_PT_testlist)
        print(BananaPi_PT_testlist)
    else:
        # If test job is for Android ,use the list of android_testlist to call
        # testcases in testcasses.py
        metafunc.parametrize("testcase_dict", android_testlist)
        print(android_testlist)

