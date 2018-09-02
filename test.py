import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess
import sys
test_path = (os.path.dirname(os.path.abspath(__file__)))
sys.path.append(test_path + '/android_testcases')
sys.path.append(test_path + '/libs')

import testcases
import adb_wrapper.adb_wrapper.adb_wrapper


def test_eval(testcase_dict,cmdopt,targetdir,variables):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    try:
        subprocess.check_output(targetdir+"/jenkins/test.sh %s"%testcase_dict,shell=True)
        result=True
    except subprocess.CalledProcessError,ex:
        print ex.output # contains stdout and stderr together 
        result=False
    assert result==True


def test_eval_android(testcase_dict,cmdopt,targetdir):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    android_ip="\'192.168.50.114\'"
    print "testcase_dict=%s"%testcase_dict
    tc="testcases.%s(%s)"%(testcase_dict,android_ip)
    print tc
    test=eval(tc)
    # try:
    #     subprocess.check_output(targetdir+"/jenkins/test.sh %s"%testcase_dict,shell=True)
    #     result=True
    # except subprocess.CalledProcessError,ex:
    #     print ex.output # contains stdout and stderr together 
    #     result=False
    # assert result==True