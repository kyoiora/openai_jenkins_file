import os
import argparse
import pdb
import sys
TARGET_DIR_ON_BOARD='/home/rk/tengine/examples/build/imagenet_classification'

def imagenet_sqz():
    target_dir=TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def imagenet_mobilenet():
    target_dir=TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n mobilenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "8.5976 - \"n02123159" in out

def imagenet_resnet50():
    target_dir=TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n resnet50 -i %s/tests/images/bike.jpg"%(target_dir,target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.9239 - \"n03792782" in out

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



def imagenet_inception_v3(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n inception_v3 "%(target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.0946 - \"n02123159" in res[0]

def imagenet_inception_v4(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n inception_v4 "%(target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.7556 - \"n02123159" in res[0]



def imagenet_vgg16(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n vgg16 -i %s/tests/images/bike.jpg"%(target_dir,target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.4998 - \"n03792782" in res[0]