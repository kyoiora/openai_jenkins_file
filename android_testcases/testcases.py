
import argparse
import pdb
import sys
from adb_wrapper.adb_wrapper.adb_wrapper import AdbWrapper
ROOT_DIR='/root/tengine_armv8/android_pack/'
TARGET_DIR_ON_BOARD='/data/local/tmp/'


# def push():

#     a = AdbWrapper() # Auto Find adb in system PATH or Environment
#     a.connect(android_ip)
#     #pdb.set_trace()
#     a.device=android_ip
#     a.push(ROOT_DIR, TARGET_DIR_ON_BOARD)
#     res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
#     print(res[0])
#     res=a.shell("cd %s && chmod u+x Classify "%(TARGET_DIR_ON_BOARD+'android_pack/'))

#     res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))

#     #pdb.set_trace()
#     print(res[0])



def imagenet_sqz(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet "%(target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.2763 - \"n02123045" in res[0]

def imagenet_alexnet(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n alexnet "%(target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.3094 - \"n02124075" in res[0]

def imagenet_googlenet(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n googlenet "%(target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.5009 - \"n02123159" in res[0]

def imagenet_mobilenet(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n mobilenet "%(target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "8.5976 - \"n02123159" in res[0]
