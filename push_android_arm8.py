import os,pdb
import sys
import pytest
import asciitable
import collections
test_path = (os.path.dirname(os.path.abspath(__file__)))
sys.path.append(test_path + '/libs')
from adb_wrapper.adb_wrapper.adb_wrapper import AdbWrapper
import argparse
TARGET_DIR_ON_BOARD='/data/local/tmp/'
ROOT_DIR='/root/tengine_armv8/tengine/android_pack/'

def push(ip_addr):
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(ip_addr)
    #pdb.set_trace()
    a.device=ip_addr
    a.root()

    res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
    res=a.shell("rm -rf %s"%(TARGET_DIR_ON_BOARD+'android_pack/*.so'))
    res=a.shell("rm -rf %s"%(TARGET_DIR_ON_BOARD+'android_pack/build'))
    res=a.shell("rm -rf %s"%(TARGET_DIR_ON_BOARD+'android_pack/Classify'))

    print res
    print 'push to board'
    a.push(ROOT_DIR,TARGET_DIR_ON_BOARD,timeout=3600)
    print 'push ok'
    print(res[0])
    res=a.shell("\'cd %s && chmod u+x Classify\' "%(TARGET_DIR_ON_BOARD+'android_pack/'))

    res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
    
    #pdb.set_trace()
    print(res[0])




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--func", help="call function", required=False,default='push')
    parser.add_argument("-ip", "--ip_addr", help="ip of device", required=True)
    args = parser.parse_args()
    if args.func=="push":
        push(ip_addr=args.ip_addr)