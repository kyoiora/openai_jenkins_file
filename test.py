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
sys.path.append(test_path + '/linux_testcases')

import testcases
import adb_wrapper.adb_wrapper.adb_wrapper
import linuxtestcases

#Linux testcase calling old test function in test.sh
def test_eval(testcase_dict,cmdopt,targetdir,variables):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])

    #eval testcases from linux_testcases.linuxtestcases.py
    print "testcase_dict=%s"%testcase_dict
    tc="linuxtestcases.%s(%s)"%(id,testcase_dict[id])
    print tc
    test=eval(tc)

    #try:
    #subprocess.check_output(targetdir+"/jenkins/test.sh %s"%testcase_dict,shell=True)
    #result=True
    #except subprocess.CalledProcessError,ex:
    #print ex.output # contains stdout and stderr together
    #result=False
    #assert result==True

#android testcase using adb to execute code in Android board
def test_eval_android(testcase_dict,cmdopt,targetdir,ip):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    android_ip="\'%s\'" %ip
    
    #eval testcases from android_testcases.testcases.py
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
