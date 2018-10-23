import pytest
import os
import asciitable
import collections
import pprint
import pdb
import subprocess
import sys
test_path = (os.path.dirname(os.path.abspath(__file__)))
sys.path.append(test_path + '/libs')

TARGET_DIR_ON_BOARD='/home/rk/tengine/examples/build/imagenet_classification'

def sqz():
    target_dir=TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

imagenet_sqz()
print "OK"