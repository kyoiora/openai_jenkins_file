import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess


def test_eval(testcase_dict,cmdopt):
    #print "testcase_id=%s,path=%s" % (id,testcase_dict[id])
    test_path=-variables[cmdopt]['root_dir']
    try:
        subprocess.check_output(test_path+"/jenkins/test.sh %s"%id,shell=True)
        result=True
    except subprocess.CalledProcessError,ex:
        print ex.output # contains stdout and stderr together 
        result=False
    assert result==True

