import pytest
import os
import asciitable
import collections
import pprint
import pdb

android_testlist=['imagenet_sqz','imagenet_alexnet','imagenet_googlenet',
                  'imagenet_mobilenet','imagenet_inception_v3',
                  'imagenet_inception_v4',
                  'imagenet_resnet50','imagenet_vgg16']

linux_testlist=['quick_api','imagenet_sqz','imagenet_alexnet','imagenet_googlenet',
                  'imagenet_mobilenet','imagenet_inception_v3',
                  'imagenet_inception_v4',
                  'imagenet_resnet50','imagenet_vgg16','ssd','mssd','yolov2','faster_rcnn','mtcnn','lighten_cnn'
                  'caffe_wrapper_sqz','vgg16_mem']

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
	if metafunc.config.getoption('cmdopt') != "adb":
		#if 'testcase_dict' in metafunc.fixturenames:
		#	test_path = metafunc.config.getoption('targetdir')
		#	testcase_list=collections.OrderedDict()
		#	print(test_path)
		#	testlist=asciitable.read(test_path+'/jenkins/core_test.list')

		#	for rec in testlist:
		#		testcase_list[rec[0]]=rec[1]
		#	pprint.pprint(dict(testcase_list.items()))
		#	metafunc.parametrize("testcase_dict", testcase_list.keys())
		metafunc.parametrize("testcase_dict", linux_testlist)
		print(linux_testlist)

	else:
		# If test job is for Android ,use the list of android_testlist to call 
		# testcases in testcasses.py
		metafunc.parametrize("testcase_dict", android_testlist)
		print(android_testlist)


