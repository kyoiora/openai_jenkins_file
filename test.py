import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess

pprint.pprint(variables)
print "cmdopt=" + cmdopt





#@pytest.mark.parametrize("id",testcase_dict)
#@pytest.mark.parametrize("id",testcase_dict.keys()[1:2])
def test_eval(testcase_dict):
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
