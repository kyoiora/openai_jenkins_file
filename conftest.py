import pytest
import os
import asciitable
import collections
import pprint
import pdb

def pytest_addoption(parser):
	parser.addoption(
		"--cmdopt", action="store", default="onboard", help="my option: onboard or cc"
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
