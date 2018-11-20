
import argparse
import pdb
import sys
import re
import prettytable as pt
from adb_wrapper.adb_wrapper.adb_wrapper import AdbWrapper
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
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n resnet50 -i %s/tests/images/bike.jpg"%(target_dir,target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.9239 - \"n03792782" in res[0]

def imagenet_vgg16(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n vgg16 -i %s/tests/images/bike.jpg"%(target_dir,target_dir,target_dir,target_dir))
    #pdb.set_trace()
    print(res[0])
    assert "0.4998 - \"n03792782" in res[0]

# Performance test for RK3399
squeezenet_FP32_1xA72=0.0
squeezenet_Int8_1xA72=0.0
squeezenet_FP32_2xA72=0.0
squeezenet_Int8_2xA72=0.0
squeezenet_FP32_1xA53=0.0
squeezenet_Int8_1xA53=0.0
squeezenet_FP32_4xA53=0.0
squeezenet_Int8_4xA53=0.0
mobilenet_FP32_1xA72=0.0
mobilenet_Int8_1xA72=0.0
mobilenet_FP32_2xA72=0.0
mobilenet_Int8_2xA72=0.0
mobilenet_FP32_1xA53=0.0
mobilenet_Int8_1xA53=0.0
mobilenet_FP32_4xA53=0.0
mobilenet_Int8_4xA53=0.0

def time_arr(arr):
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    a=re.findall(r"\d+\.?\d*", arr[Number])
    return a

def squeezenet_FP32_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res[0])
    arr=res[0].splitlines()
    global squeezenet_FP32_1xA72
    a=time_arr(arr)
    squeezenet_FP32_1xA72=a[1]

def squeezenet_Int8_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_1xA72
    a=time_arr(arr)
    squeezenet_Int8_1xA72=a[1]

def squeezenet_FP32_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_2xA72
    a=time_arr(arr)
    squeezenet_FP32_2xA72=a[1]

def squeezenet_Int8_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_2xA72
    a=time_arr(arr)
    squeezenet_Int8_2xA72=a[1]

def squeezenet_FP32_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_1xA53
    a=time_arr(arr)
    squeezenet_FP32_1xA53=a[1]

def squeezenet_Int8_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_1xA53
    a=time_arr(arr)
    squeezenet_Int8_1xA53=a[1]

def squeezenet_FP32_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_4xA53
    a=time_arr(arr)
    squeezenet_FP32_4xA53=a[1]

def squeezenet_Int8_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_4xA53
    a=time_arr(arr)
    squeezenet_Int8_4xA53=a[1]

def mobilenet_FP32_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_1xA72
    a=time_arr(arr)
    mobilenet_FP32_1xA72=a[1]

def mobilenet_Int8_1xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_1xA72
    a=time_arr(arr)
    mobilenet_Int8_1xA72=a[1]

def mobilenet_FP32_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_2xA72
    a=time_arr(arr)
    mobilenet_FP32_2xA72=a[1]

def mobilenet_Int8_2xA72(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=4,5;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_2xA72
    a=time_arr(arr)
    mobilenet_Int8_2xA72=a[1]

def mobilenet_FP32_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_1xA53
    a=time_arr(arr)
    mobilenet_FP32_1xA53=a[1]

def mobilenet_Int8_1xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_1xA53
    a=time_arr(arr)
    mobilenet_Int8_1xA53=a[1]

def mobilenet_FP32_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_4xA53
    a=time_arr(arr)
    mobilenet_FP32_4xA53=a[1]

def mobilenet_Int8_4xA53(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_4xA53
    a=time_arr(arr)
    mobilenet_Int8_4xA53=a[1]


def RK3399_testresult(targetdir,cmdopt):
    RK3399 = pt.PrettyTable()
    RK3399.field_names = ["models","FP32_1xA72", "Int8_1xA72", "FP32_2xA72", "Int8_2xA72","FP32_1xA53", "Int8_1xA53", "FP32_4xA53", "Int8_4xA53"]
    RK3399.add_row(["squeezenet",squeezenet_FP32_1xA72,squeezenet_Int8_1xA72,squeezenet_FP32_2xA72,squeezenet_Int8_2xA72,squeezenet_FP32_1xA53,squeezenet_Int8_1xA53,squeezenet_FP32_4xA53,squeezenet_Int8_4xA53])
    RK3399.add_row(["mobilenet",mobilenet_FP32_1xA72,mobilenet_Int8_1xA72,mobilenet_FP32_2xA72,mobilenet_Int8_2xA72,mobilenet_FP32_1xA53,mobilenet_Int8_1xA53,mobilenet_FP32_4xA53,mobilenet_Int8_4xA53])
    print(RK3399)

# Performance test for RK3288

squeezenet_FP32_1xA17=0.0
squeezenet_Int8_1xA17=0.0
squeezenet_FP32_4xA17=0.0
squeezenet_Int8_4xA17=0.0

mobilenet_FP32_1xA17=0.0
mobilenet_Int8_1xA17=0.0
mobilenet_FP32_4xA17=0.0
mobilenet_Int8_4xA17=0.0


def squeezenet_FP32_1xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_1xA17
    a=time_arr(arr)
    squeezenet_FP32_1xA17=a[1]

def squeezenet_Int8_1xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_1xA17
    a=time_arr(arr)
    squeezenet_Int8_1xA17=a[1]

def squeezenet_FP32_4xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_4xA17
    a=time_arr(arr)
    squeezenet_FP32_4xA17=a[1]

def squeezenet_Int8_4xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_4xA17
    a=time_arr(arr)
    squeezenet_Int8_4xA17=a[1]


def mobilenet_FP32_1xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_1xA17
    a=time_arr(arr)
    mobilenet_FP32_1xA17=a[1]

def mobilenet_Int8_1xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_1xA17
    a=time_arr(arr)
    mobilenet_Int8_1xA17=a[1]

def mobilenet_FP32_4xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_4xA17
    a=time_arr(arr)
    mobilenet_FP32_4xA17=a[1]

def mobilenet_Int8_4xA17(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_4xA17
    a=time_arr(arr)
    mobilenet_Int8_4xA17=a[1]


def RK3288_testresult(targetdir,cmdopt):
    RK3288 = pt.PrettyTable()
    RK3288.field_names = ["models","FP32_1xA17", "Int8_1xA17", "FP32_4xA17", "Int8_4xA17"]
    RK3288.add_row(["squeezenet",squeezenet_FP32_1xA17,squeezenet_Int8_1xA17,squeezenet_FP32_4xA17,squeezenet_Int8_4xA17])
    RK3288.add_row(["mobilenet",mobilenet_FP32_1xA17,mobilenet_Int8_1xA17,mobilenet_FP32_4xA17,mobilenet_Int8_4xA17])
    print(RK3288)

# Performance test for Bananapi

squeezenet_FP32_1xA7=0.0
squeezenet_Int8_1xA7=0.0
squeezenet_FP32_4xA7=0.0
squeezenet_Int8_4xA7=0.0

mobilenet_FP32_1xA7=0.0
mobilenet_Int8_1xA7=0.0
mobilenet_FP32_4xA7=0.0
mobilenet_Int8_4xA7=0.0


def squeezenet_FP32_1xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_1xA7
    a=time_arr(arr)
    squeezenet_FP32_1xA7=a[1]

def squeezenet_Int8_1xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_1xA7
    a=time_arr(arr)
    squeezenet_Int8_1xA7=a[1]

def squeezenet_FP32_4xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_FP32_4xA7
    a=time_arr(arr)
    squeezenet_FP32_4xA7=a[1]

def squeezenet_Int8_4xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n squeezenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global squeezenet_Int8_4xA7
    a=time_arr(arr)
    squeezenet_Int8_4xA7=a[1]


def mobilenet_FP32_1xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_1xA7
    a=time_arr(arr)
    mobilenet_FP32_1xA7=a[1]

def mobilenet_Int8_1xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=2;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_1xA7
    a=time_arr(arr)
    mobilenet_Int8_1xA7=a[1]

def mobilenet_FP32_4xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_FP32_4xA7
    a=time_arr(arr)
    mobilenet_FP32_4xA7=a[1]

def mobilenet_Int8_4xA7(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=0,1,2,3;export LD_LIBRARY_PATH=.;./Classify -n mobilenet -r 100"%(target_dir))
    print(res)
    arr=res.splitlines()
    global mobilenet_Int8_4xA7
    a=time_arr(arr)
    mobilenet_Int8_4xA7=a[1]


def Bananapi_testresult(targetdir,cmdopt):
    Bananapi = pt.PrettyTable()
    Bananapi.field_names = ["models","FP32_1xA7", "Int8_1xA7", "FP32_4xA7", "Int8_4xA7"]
    Bananapi.add_row(["squeezenet",squeezenet_FP32_1xA7,squeezenet_Int8_1xA7,squeezenet_FP32_4xA7,squeezenet_Int8_4xA7])
    Bananapi.add_row(["mobilenet",mobilenet_FP32_1xA7,mobilenet_Int8_1xA7,mobilenet_FP32_4xA7,mobilenet_Int8_4xA7])
    print(Bananapi)
