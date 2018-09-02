import os,pdb
import sys
test_path = (os.path.dirname(os.path.abspath(__file__)))
sys.path.append(test_path + '/libs')
from adb_wrapper.adb_wrapper.adb_wrapper import AdbWrapper
import argparse
ROOT_DIR='/root/tengine_armv8/android_pack/'
TARGET_DIR_ON_BOARD='/data/local/tmp/'
def push():
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect("192.168.50.114")
    #pdb.set_trace()
    a.device='192.168.50.114'

    res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
    res=a.shell("rm -rf %s"%(TARGET_DIR_ON_BOARD+'android_pack/*.so'))

    res=a.shell("rm -rf %s"%(TARGET_DIR_ON_BOARD+'android_pack/Classify'))


    a.push(ROOT_DIR, TARGET_DIR_ON_BOARD)

    print(res[0])
    res=a.shell("\'cd %s && chmod u+x Classify\' "%(TARGET_DIR_ON_BOARD+'android_pack/'))

    res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
    
    #pdb.set_trace()
    print(res[0])




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--func", help="call function", required=False)
    args = parser.parse_args()
    if args.func=="push":
        push()