import pytest
import os
import asciitable
import collections
import pprint
import pdb

android_testlist=['Classify1','Classify2']

def pytest_addoption(parser):
	parser.addoption(
		"--cmdopt", action="store", default="onboard", help="my option: onboard or cc or adb"
	)
	parser.addoption(
		"--targetdir", action="store", default="/root/tengine/", help="dir of target targetdir"
	)

@pytest.fixture
def cmdopt(request):
	return request.config.getoption("--cmdopt")

@pytest.fixture
def targetdir(request):
	return request.config.getoption("--targetdir")

def pytest_generate_tests(metafunc):
	print metafunc.config.getoption('cmdopt')
	if metafunc.config.getoption('cmdopt') != "adb":
		if 'testcase_dict' in metafunc.fixturenames:
			test_path = metafunc.config.getoption('targetdir')
			testcase_list=collections.OrderedDict()
			print(test_path)
			testlist=asciitable.read(test_path+'/jenkins/core_test.list')

			for rec in testlist:
				testcase_list[rec[0]]=rec[1]
				#pdb.set_trace()
			pprint.pprint(dict(testcase_list.items()))
			metafunc.parametrize("testcase_dict", testcase_list.keys())
			#metafunc.parametrize("type_name", metafunc.config.getoption('cmdopt'))
			#pdb.set_trace()
	else:

		metafunc.parametrize("testcase_dict", android_testlist)
		print(android_testlist)


