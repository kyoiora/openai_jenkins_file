
import argparse
import pdb
import sys
from adb_wrapper.adb_wrapper.adb_wrapper import AdbWrapper
ROOT_DIR='/root/tengine_armv8/android_pack/'
TARGET_DIR_ON_BOARD='/data/local/tmp/'
import logging


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

def imagenet_resnet50(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n resnet50 -i %s/tests/images/bike.jpg"%(target_dir,target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.9239 - \"n03792782" in res[0]

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

# Performance test
def squeezenet_FP32_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_Int8_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_FP32_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_Int8_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_FP32_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_Int8_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_FP32_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def squeezenet_Int8_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_FP32_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_Int8_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_FP32_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_Int8_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_FP32_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_Int8_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_FP32_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])

def mobilenet_Int8_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    #pdb.set_trace()
    arr=res[0].splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    print(arr[Number])
