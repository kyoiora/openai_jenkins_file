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



def pytest_generate_tests(metafunc):
	if 'testcase_dict' in metafunc.fixturenames:
		if metafunc.config.getoption('cmdopt') == "onboard":
			test_path = '/root/tengine/jenkins'
		elif metafunc.config.getoption('cmdopt') == "cc":
			test_path = '/root/cross_test/jenkins'
		testcase_list=collections.OrderedDict()
		print(test_path)
		testlist=asciitable.read(test_path+'/core_test.list')

		for rec in testlist:
			testcase_list[rec[0]]=rec[1]
			#pdb.set_trace()
		pprint.pprint(dict(testcase_list.items()))
		metafunc.parametrize("testcase_dict", testcase_list.keys())
		metafunc.parametrize("cmdopt", metafunc.config.getoption('cmdopt'))
		#pdb.set_trace()
