
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

def ssd(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    test_dir=target_dir+'/build/ssd/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s./SSD "%(target_dir,target_dir,test_dir))
    print(res[0])
    arr=res[0].splitlines()
    for char in arr:
        if "car" in char:
            char_arr=char.splitlines()
            carNumber=arr.index(char_arr[0])+1
        if "bicycle" in char:
            char_arr=char.splitlines()
            bicycleNumber=arr.index(char_arr[0])+1
        if "dog" in char:
            char_arr=char.splitlines()
            dogNumber=arr.index(char_arr[0])+1
    #check the car
    a=re.findall(r"\d+\.?\d*", arr[carNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=475),"car x0 more than 475"
    assert(x0>=465),"car x0 less than 465"
    assert(y0<=90),"car y0 more than 90"
    assert(y0>=80),"car y0 less than 80"
    assert(x1<=701),"car x1 more than 701"
    assert(x1>=691),"car x1 less than 691"
    assert(y1<=176),"car y1 more than 176"
    assert(y1>=166),"car y1 less than 166"
    #check the bicycle
    a=re.findall(r"\d+\.?\d*", arr[bicycleNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=148),"bicycle x0 more than 148"
    assert(x0>=138),"bicycle x0 less than 138"
    assert(y0<=143),"bicycle y0 more than 143"
    assert(y0>=133),"bicycle y0 less than 133"
    assert(x1<=584),"bicycle x1 more than 584"
    assert(x1>=574),"bicycle x1 less than 574"
    assert(y1<=509),"bicycle y1 more than 509"
    assert(y1>=499),"bicycle y1 less than 499"
    #check the dog
    a=re.findall(r"\d+\.?\d*", arr[dogNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=137),"dog x0 more than 137"
    assert(x0>=127),"dog x0 less than 127"
    assert(y0<=224),"dog y0 more than 224"
    assert(y0>=214),"dog y0 less than 214"
    assert(x1<=339),"dog x1 more than 339"
    assert(x1>=329),"dog x1 less than 329"
    assert(y1<=538),"dog y1 more than 538"
    assert(y1>=528),"dog y1 less than 528"

def mssd(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    test_dir=target_dir+'/build/mobilenet_ssd/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip


    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s./MSSD "%(target_dir,target_dir,test_dir))
    print(res[0])
    arr=res[0].splitlines()
    for char in arr:
        if "car" in char:
            char_arr=char.splitlines()
            carNumber=arr.index(char_arr[0])+1
        if "bicycle" in char:
            char_arr=char.splitlines()
            bicycleNumber=arr.index(char_arr[0])+1
        if "dog" in char:
            char_arr=char.splitlines()
            dogNumber=arr.index(char_arr[0])+1
    #check the car
    a=re.findall(r"\d+\.?\d*", arr[carNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=475),"car x0 more than 475"
    assert(x0>=465),"car x0 less than 465"
    assert(y0<=77),"car y0 more than 77"
    assert(y0>=67),"car y0 less than 67"
    assert(x1<=693),"car x1 more than 693"
    assert(x1>=683),"car x1 less than 683"
    assert(y1<=176),"car y1 more than 176"
    assert(y1>=166),"car y1 less than 166"
    #check the bicycle
    a=re.findall(r"\d+\.?\d*", arr[bicycleNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=111),"bicycle x0 more than 111"
    assert(x0>=101),"bicycle x0 less than 101"
    assert(y0<=143),"bicycle y0 more than 143"
    assert(y0>=133),"bicycle y0 less than 133"
    assert(x1<=580),"bicycle x1 more than 580"
    assert(x1>=570),"bicycle x1 less than 570"
    assert(y1<=420),"bicycle y1 more than 420"
    assert(y1>=411),"bicycle y1 less than 411"
    #check the dog
    a=re.findall(r"\d+\.?\d*", arr[dogNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=143),"dog x0 more than 143"
    assert(x0>=133),"dog x0 less than 133"
    assert(y0<=214),"dog y0 more than 214"
    assert(y0>=204),"dog y0 less than 204"
    assert(x1<=329),"dog x1 more than 329"
    assert(x1>=320),"dog x1 less than 320"
    assert(y1<=548),"dog y1 more than 548"
    assert(y1>=538),"dog y1 less than 538"

def yolov2(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    test_dir=target_dir+'/build/yolov2/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s./YOLOV2 "%(target_dir,target_dir,test_dir))
    print(res[0])
    arr=res[0].splitlines()
    for char in arr:
        if "car" in char:
            char_arr=char.splitlines()
            carNumber=arr.index(char_arr[0])+1
        if "bicycle" in char:
            char_arr=char.splitlines()
            bicycleNumber=arr.index(char_arr[0])+1
        if "dog" in char:
            char_arr=char.splitlines()
            dogNumber=arr.index(char_arr[0])+1
    #check the car
    a=re.findall(r"\d+\.?\d*", arr[carNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<450),"car x0 more than 450"
    assert(x0>440),"car x0 less than 440"
    assert(y0<78),"car y0 more than 78"
    assert(y0>68),"car y0 less than 68"
    assert(x1<680),"car x1 more than 680"
    assert(x1>670),"car x1 less than 670"
    assert(y1<181),"car y1 more than 181"
    assert(y1>171),"car y1 less than 171"
    #check the bicycle
    a=re.findall(r"\d+\.?\d*", arr[bicycleNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<126),"bicycle x0 more than 126"
    assert(x0>116),"bicycle x0 less than 116"
    assert(y0<148),"bicycle y0 more than 148"
    assert(y0>138),"bicycle y0 less than 138"
    assert(x1<562),"bicycle x1 more than 562"
    assert(x1>552),"bicycle x1 less than 552"
    assert(y1<445),"bicycle y1 more than 445"
    assert(y1>435),"bicycle y1 less than 435"
    #check the dog
    a=re.findall(r"\d+\.?\d*", arr[dogNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<124),"dog x0 more than 124"
    assert(x0>114),"dog x0 less than 114"
    assert(y0<184),"dog y0 more than 184"
    assert(y0>174),"dog y0 less than 174"
    assert(x1<328),"dog x1 more than 328"
    assert(x1>318),"dog x1 less than 318"
    assert(y1<550),"dog y1 more than 550"
    assert(y1>540),"dog y1 less than 540"

def faster_rcnn(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    test_dir=target_dir+'/build/faster_rcnn/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s./FASTER_RCNN"%(target_dir,target_dir,test_dir))
    print(res[0])
    arr=res[0].splitlines()
    for char in arr:
        if "car" in char:
            char_arr=char.splitlines()
            carNumber=arr.index(char_arr[0])+1
        if "bicycle" in char:
            char_arr=char.splitlines()
            bicycleNumber=arr.index(char_arr[0])+1
        if "dog" in char:
            char_arr=char.splitlines()
            dogNumber=arr.index(char_arr[0])+1
    #check the car
    a=re.findall(r"\d+\.?\d*", arr[carNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=436),"car x0 more than 436"
    assert(x0>=426),"car x0 less than 426"
    assert(y0<=84),"car y0 more than 84"
    assert(y0>=74),"car y0 less than 74"
    assert(x1<=696),"car x1 more than 696"
    assert(x1>=686),"car x1 less than 686"
    assert(y1<=166),"car y1 more than 166"
    assert(y1>=156),"car y1 less than 156"
    #check the dog
    a=re.findall(r"\d+\.?\d*", arr[dogNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=102),"dog x0 more than 102"
    assert(x0>=92),"dog x0 less than 92"
    assert(y0<=228),"dog y0 more than 228"
    assert(y0>=218),"dog y0 less than 218"
    assert(x1<=363),"dog x1 more than 363"
    assert(x1>=353),"dog x1 less than 353"
    assert(y1<=551),"dog y1 more than 551"
    assert(y1>=541),"dog y1 less than 541"

def mtcnn(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    test_dir=target_dir+'/build/mtcnn/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s./MTCNN"%(target_dir,target_dir,test_dir))
    print(res[0])
    arr=res[0].splitlines()
    for char in arr:
        if "face" in char:
            char_arr=char.splitlines()
            firstBoxNumber=arr.index(char_arr[0])+1
            secondBoxNumber=arr.index(char_arr[0])+2
            thirdBoxNumber=arr.index(char_arr[0])+3
            fourBoxNumber=arr.index(char_arr[0])+4
    #check the first BOX
    a=re.findall(r"\d+\.?\d*", arr[firstBoxNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=174),"firstBox x0 more than 174"
    assert(x0>=164),"firstBox x0 less than 164"
    assert(y0<=86),"firstBox more than 86"
    assert(y0>=76),"firstBox less than 76"
    assert(x1<=211),"firstBoxN more than 211"
    assert(x1>=201),"firstBox less than 201"
    assert(y1<=140),"firstBoxN more than 140"
    assert(y1>=130),"firstBox less than 130"
    #check the second BOX
    a=re.findall(r"\d+\.?\d*", arr[secondBoxNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=48),"secondBoxN x0 more than 48"
    assert(x0>=38),"secondBox x0 less than 38"
    assert(y0<=91),"secondBox y0 more than 91"
    assert(y0>=81),"secondBox y0 less than 81"
    assert(x1<=90),"secondBox x1 more than 90"
    assert(x1>=80),"secondBox x1 less than 80"
    assert(y1<=154),"secondBox y1 more than 154"
    assert(y1>=144),"secondBox y1 less than 144"
    #check the third BOX
    a=re.findall(r"\d+\.?\d*", arr[thirdBoxNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=297),"thirdBox x0 more than 297"
    assert(x0>=287),"thirdBox x0 less than 287"
    assert(y0<=108),"thirdBox y0 more than 108"
    assert(y0>=98),"thirdBox y0 less than 98"
    assert(x1<=329),"thirdBox x1 more than 329"
    assert(x1>=319),"thirdBox x1 less than 319"
    assert(y1<=155),"thirdBox y1 more than 155"
    assert(y1>=145),"thirdBox y1 less than 145"
    #check the four BOX
    a=re.findall(r"\d+\.?\d*", arr[fourBoxNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<=384),"fourBox x0 more than 384"
    assert(x0>=374),"fourBox x0 less than 374"
    assert(y0<=61),"fourBox y0 more than 61"
    assert(y0>=51),"fourBox y0 less than 51"
    assert(x1<=465),"fourBox x1 more than 465"
    assert(x1>=455),"fourBox x1 less than 455"
    assert(y1<=150),"fourBox y1 more than 150"
    assert(y1>=140),"fourBox y1 less than 140"


def lighten_cnn(android_ip):
    target_dir=TARGET_DIR_ON_BOARD+'android_pack'
    test_dir=target_dir+'/build/lighten_cnn/'
    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip

    res=a.shell("cd %s;export LD_LIBRARY_PATH=%s; %s./LIGHTEN_CNN"%(target_dir,target_dir,test_dir))
    print(res[0])
    arr=res[0].splitlines()
    for char in arr:
        if "maxError" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    #check the car
    a=re.findall(r"\d+\.?\d*", arr[Number])
    x0=float(a[0])
    assert(x0>=0.00001),"car x0 less than 0.00001"

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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
    global mobilenet_Int8_4xA53
    a=time_arr(arr)
    mobilenet_Int8_4xA53=a[1]


def RK3399_testresult(android_ip):
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
    global mobilenet_Int8_4xA17
    a=time_arr(arr)
    mobilenet_Int8_4xA17=a[1]


def RK3288_testresult(android_ip):
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
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
    print(res[0])
    arr=res[0].splitlines()
    global mobilenet_Int8_4xA7
    a=time_arr(arr)
    mobilenet_Int8_4xA7=a[1]


def Bananapi_testresult(android_ip):
    Bananapi = pt.PrettyTable()
    Bananapi.field_names = ["models","FP32_1xA7", "Int8_1xA7", "FP32_4xA7", "Int8_4xA7"]
    Bananapi.add_row(["squeezenet",squeezenet_FP32_1xA7,squeezenet_Int8_1xA7,squeezenet_FP32_4xA7,squeezenet_Int8_4xA7])
    Bananapi.add_row(["mobilenet",mobilenet_FP32_1xA7,mobilenet_Int8_1xA7,mobilenet_FP32_4xA7,mobilenet_Int8_4xA7])
    print(Bananapi)
