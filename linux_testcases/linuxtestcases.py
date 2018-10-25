import os
import re
ROOT_DIR='/home/rk/tengine/'
TARGET_DIR_ON_BOARD='examples/build/imagenet_classification'

def imagenet_sqz():
    target_dir=ROOT_DIR+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def imagenet_mobilenet():
    target_dir=ROOT_DIR+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n mobilenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "8.5976 - \"n02123159" in out

def imagenet_resnet50():
    target_dir=ROOT_DIR
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n resnet50 -i %s/tests/images/bike.jpg"%(target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.9239 - \"n03792782" in out

def imagenet_googlenet():
    target_dir=ROOT_DIR+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n googlenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.5009 - \"n02123159" in out

def imagenet_inceptionv4():
    target_dir=ROOT_DIR+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n inception_v4 "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.7556 - \"n02123159" in out

def imagenet_inceptionv3():
    target_dir=ROOT_DIR+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n inception_v3 "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.0946 - \"n02123159" in out

def imagenet_alexnet():
    target_dir=ROOT_DIR+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n alexnet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.3094 - \"n02124075" in out

def imagenet_vgg16():
    target_dir=ROOT_DIR
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n vgg16 -i %s/tests/images/bike.jpg"%(target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.4998 - \"n03792782" in out

def ssd():
    target_dir=ROOT_DIR+'build/examples/ssd/'
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s./SSD "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    arr=out.splitlines()
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
    assert(x0<476),"car x0 more than 475"
    assert(x0>464),"car x0 less than 465"
    assert(y0<91),"car y0 more than 90"
    assert(y0>79),"car y0 less than 80"
    assert(x1<702),"car x1 more than 701"
    assert(x1>690),"car x1 less than 691"
    assert(y1<177),"car y1 more than 176"
    assert(y1>165),"car y1 less than 166"
    #check the bicycle
    a=re.findall(r"\d+\.?\d*", arr[bicycleNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<149),"bicycle x0 more than 148"
    assert(x0>137),"bicycle x0 less than 138"
    assert(y0<144),"bicycle y0 more than 143"
    assert(y0>132),"bicycle y0 less than 133"
    assert(x1<585),"bicycle x1 more than 584"
    assert(x1>573),"bicycle x1 less than 574"
    assert(y1<510),"bicycle y1 more than 509"
    assert(y1>498),"bicycle y1 less than 499"
    #check the dog
    a=re.findall(r"\d+\.?\d*", arr[dogNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<138),"dog x0 more than 137"
    assert(x0>126),"dog x0 less than 127"
    assert(y0<225),"dog y0 more than 224"
    assert(y0>213),"dog y0 less than 214"
    assert(x1<340),"dog x1 more than 339"
    assert(x1>328),"dog x1 less than 329"
    assert(y1<539),"dog y1 more than 538"
    assert(y1>527),"dog y1 less than 528"

def mssd():
    target_dir=ROOT_DIR+'build/examples/mobilenet_ssd/'
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s./MSSD "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    arr=out.splitlines()
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
    assert(x0<476),"car x0 more than 475"
    assert(x0>464),"car x0 less than 465"
    assert(y0<78),"car y0 more than 77"
    assert(y0>66),"car y0 less than 67"
    assert(x1<694),"car x1 more than 693"
    assert(x1>682),"car x1 less than 683"
    assert(y1<177),"car y1 more than 176"
    assert(y1>165),"car y1 less than 166"
    #check the bicycle
    a=re.findall(r"\d+\.?\d*", arr[bicycleNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<112),"bicycle x0 more than 111"
    assert(x0>100),"bicycle x0 less than 101"
    assert(y0<144),"bicycle y0 more than 143"
    assert(y0>132),"bicycle y0 less than 133"
    assert(x1<581),"bicycle x1 more than 580"
    assert(x1>569),"bicycle x1 less than 570"
    assert(y1<421),"bicycle y1 more than 420"
    assert(y1>410),"bicycle y1 less than 411"
    #check the dog
    a=re.findall(r"\d+\.?\d*", arr[dogNumber])
    x0=float(a[0])
    y0=float(a[1])
    x1=float(a[2])
    y1=float(a[3])
    assert(x0<144),"dog x0 more than 143"
    assert(x0>132),"dog x0 less than 133"
    assert(y0<215),"dog y0 more than 214"
    assert(y0>203),"dog y0 less than 204"
    assert(x1<330),"dog x1 more than 329"
    assert(x1>319),"dog x1 less than 320"
    assert(y1<549),"dog y1 more than 548"
    assert(y1>537),"dog y1 less than 538"

def yolov2():
    target_dir=ROOT_DIR+'build/examples/yolov2/'
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s./YOLOV2 "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    arr=out.splitlines()
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