import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess


def test_eval(testcase_dict,cmdopt,targetdir,variables):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    try:
        subprocess.check_output(targetdir+"/jenkins/test.sh %s"%testcase_dict,shell=True)
        result=True
    except subprocess.CalledProcessError,ex:
        print ex.output # contains stdout and stderr together 
        result=False
    assert result==True

