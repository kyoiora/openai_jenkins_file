import os
import re
TARGET_DIR_ON_BOARD='/examples/build/imagenet_classification'
caffe_wrapper_sqz_dir='/examples/build/caffe_wrapper/cpp_classification'
import prettytable as pt

# Performance test for RT3399

def time_result(arr):
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    a=re.findall(r"\d+\.?\d*", arr[Number])

def squeezenet_FP32_1xA72(targetdir,cmdopt):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export KERNEL_MODE=0;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet -r 100 & mpstat -P ALL 1 3;sleep 20"%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print("FP32_1xA72 result:\n")
    print(out)
    arr=out.splitlines()
    for char in arr:
        if "Repeat" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    a1=re.findall(r"\d+\.?\d*", arr[Number])
    FP32_1xA72_time=a1[1]

    res=os.popen("cd %s;export KERNEL_MODE=2;export TENGINE_CPU_LIST=5;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet -r 100 & mpstat -P ALL 1 3;sleep 20"%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print("Int8_1xA72 result:\n")
    print(out)
    arr=out.splitlines()
    a=time_result(arr)
    Int8_1xA72_time=a[1]
    RK3399 = pt.PrettyTable()
    RK3399.field_names = ["FP32_1xA72", "Int8_1xA72", "FP32_2xA72", "Int8_2xA72","FP32_1xA53", "Int8_1xA53", "FP32_4xA53", "Int8_4xA53"]
    RK3399.add_row([FP32_1xA72,100,200,199,198,11,11,11])
    print(RK3399)
