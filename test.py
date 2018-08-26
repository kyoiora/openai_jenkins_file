import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess

pprint.pprint(variables)
print "cmdopt=" + cmdopt

if cmdopt == "onboard":
    test_path = '/root/tengine/jenkins'
elif cmdopt == "cc":
    test_path = '/root/cross_test'
testcase_dict=collections.OrderedDict()
print(test_path)
testlist=asciitable.read(test_path+'/core_test.list')

for rec in testlist:
    testcase_dict[rec[0]]=rec[1]
    #pdb.set_trace()
pprint.pprint(dict(testcase_dict.items()))



@pytest.mark.parametrize("id",testcase_dict.keys())
#@pytest.mark.parametrize("id",testcase_dict.keys()[1:2])
def test_eval(self,id):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    global test_path
    global cmdopt
    if cmdopt == "onboard":
        try:
            subprocess.check_output(test_path+"/test.sh %s"%id,shell=True)
            result=True
        except subprocess.CalledProcessError,ex:
            print ex.output # contains stdout and stderr together 
            result=False
        assert result==True
    elif cmdopt == "cc":
        try:
            subprocess.check_output(test_path+"/test.sh %s"%id,shell=True)
            result=True
        except subprocess.CalledProcessError,ex:
            print ex.output # contains stdout and stderr together 
            result=False
        assert result==True
