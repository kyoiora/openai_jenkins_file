import os
import re

TARGET_DIR_ON_BOARD='/examples/build/imagenet_classification'
caffe_wrapper_sqz_dir='/build/examples/caffe_wrapper/cpp_classification'

def quick_api(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;./build/internal/bin/test_quick_api"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def test_dev(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;./build/internal/bin/test_dev"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def test_two_dev(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;./build/internal/bin/test_two_dev"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def test_two_sqz(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;./build/internal/bin/test_two_sqz"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def get_node(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;./build/internal/bin/test_get_node"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def test_mxnet_mobilenet(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s; ./build/tests/bin/test_mxnet_mobilenet"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "8.0579 - \"n02124075" in out

def test_onnx_sqz(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s; ./build/tests/bin/test_onnx_sqz"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.7178 - \"n02123045" in out

def test_tf_mobilenet(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s; ./build/tests/bin/test_tf_mobilenet"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.5246 - \"n02123394" in out

def test_tf_inceptionv3(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s; ./build/tests/bin/test_tf_inceptionv3"%(target_dir),"r")
    out=res.read()
    print(out)
    assert "0.7361 - \"military uniform" in out

def imagenet_sqz(targetdir):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def imagenet_mobilenet(targetdir):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n mobilenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "8.5976 - \"n02123159" in out

def imagenet_resnet50(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n resnet50 -i %s/tests/images/bike.jpg"%(target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.9239 - \"n03792782" in out

def imagenet_googlenet(targetdir):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n googlenet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.5009 - \"n02123159" in out

def imagenet_inception_v4(targetdir):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n inception_v4 "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.7556 - \"n02123159" in out

def imagenet_inception_v3(targetdir):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n inception_v3 "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.0946 - \"n02123159" in out

def imagenet_alexnet(targetdir):
    target_dir=targetdir+TARGET_DIR_ON_BOARD
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n alexnet "%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.3094 - \"n02124075" in out

def imagenet_vgg16(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n vgg16 -i %s/tests/images/bike.jpg"%(target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir+TARGET_DIR_ON_BOARD,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.4998 - \"n03792782" in out

def ssd(targetdir):
    target_dir=targetdir+'/build/examples/ssd/'
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

def mssd(targetdir):
    target_dir=targetdir+'/build/examples/mobilenet_ssd/'
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

def yolov2(targetdir):
    target_dir=targetdir+'/build/examples/yolov2/'
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

def faster_rcnn(targetdir):
    target_dir=targetdir+'/build/examples/faster_rcnn/'
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s./FASTER_RCNN"%(target_dir,target_dir,target_dir),"r")
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

def mtcnn(targetdir):
    target_dir=targetdir+'/build/examples/mtcnn/'
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s./MTCNN"%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    arr=out.splitlines()
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


def lighten_cnn(targetdir):
    target_dir=targetdir+'/build/examples/lighten_cnn/'
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s; %s./LIGHTEN_CNN"%(target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    arr=out.splitlines()
    for char in arr:
        if "maxError" in char:
            char_arr=char.splitlines()
            Number=arr.index(char_arr[0])
    #check the car
    a=re.findall(r"\d+\.?\d*", arr[Number])
    x0=float(a[0])
    assert(x0>=0.00001),"car x0 less than 0.00001"


def caffe_wrapper_sqz(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s;./classification %s/models/sqz.prototxt %s/models/squeezenet_v1.1.caffemodel %s/examples/caffe_wrapper/cpp_classification/imagenet_mean.binaryproto %s/models/synset_words.txt %s/tests/images/cat.jpg"%(target_dir+caffe_wrapper_sqz_dir,target_dir+caffe_wrapper_sqz_dir,target_dir,target_dir,target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.2763 - \"n02123045" in out

def caffe_wrapper_mobilenet(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s;export LD_LIBRARY_PATH=%s;./classification_mobilenet %s/models/mobilenet_deploy.prototxt %s/models/mobilenet.caffemodel %s/examples/caffe_wrapper/cpp_classification/imagenet_mean.binaryproto %s/models/synset_words.txt %s/tests/images/cat.jpg"%(target_dir+caffe_wrapper_sqz_dir,target_dir+caffe_wrapper_sqz_dir,target_dir,target_dir,target_dir,target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "8.5976 - \"n02123159" in out

def caffe_wrapper_mtcnn_4faces(targetdir):
    root_dir=targetdir
    target_dir=targetdir+'/build/examples/caffe_wrapper/mtcnn'
    cmd1="export TENGINE_CONFIG_FILE=%s/install/etc/tengine/config"%(root_dir)
    cmd2="echo \"face 0: x0,y0 169.23715 84.18719  x1,y1 205.29367  134.34718\" >> /tmp/master.dummy"
    cmd3="echo \"face 1: x0,y0 42.22129 84.22765  x1,y1 84.91341  148.80046\" >> /tmp/master.dummy"
    cmd4="echo \"face 2: x0,y0 290.14917 102.54037  x1,y1 324.89871  151.54451\" >> /tmp/master.dummy"
    cmd5="echo \"face 3: x0,y0 376.13626 51.77087  x1,y1 464.53513  144.84897\" >> /tmp/master.dummy"
    cmd6="echo \"total detected: 4 faces\" >> /tmp/master.dummy"
    cmd=cmd1+"&&"+cmd2+"&&"+cmd3+"&&"+cmd4+"&&"+cmd5+"&&"+cmd6
    os.system(cmd)
    target_dir=targetdir+'/build/examples/caffe_wrapper/mtcnn'
    os.popen("cd %s;echo ./CAFFE_MTCNN %s/tests/images/mtcnn_face4.jpg %s/models wrapper_result4.jpg;./CAFFE_MTCNN %s/tests/images/mtcnn_face4.jpg %s/models wrapper_result4.jpg | grep face > /tmp/result.dummy"%(target_dir,root_dir,root_dir,root_dir,root_dir),"r")
    line1=os.popen("cat /tmp/master.dummy","r")
    out1=line1.read()
    print(out1)
    line2=os.popen("cat /tmp/result.dummy","r")
    out2=line2.read()
    print(out2)
    assert(out1!=out2)

    arr=out2.splitlines()
    os.system("rm /tmp/result.dummy;rm /tmp/master.dummy")
    for char in arr:
        if "face 0" in char:
        #find face0 and change the face 0 to list
            char_arr=char.splitlines()
        #index face0Number in arr
            face0Number=arr.index(char_arr[0])
            face1Number=arr.index(char_arr[0])+1
            face2Number=arr.index(char_arr[0])+2
            face3Number=arr.index(char_arr[0])+3

    #check face0
    a=re.findall(r"\d+\.?\d*", arr[face0Number])
    print a
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=168),"face0 x0 less than 168"
    assert(x0<=170),"face0 x0 more than 170"
    assert(y0>=83),"face0 y0 less than 83"
    assert(y0<=85),"face0 y0 more than 85"
    assert(x1>=204),"face0 x1 less than 204"
    assert(x1<=206),"face0 x1 more than 206"
    assert(y1>=133),"face0 y1 less than 133"
    assert(y1<=135),"face0 y1 more than 135"
    #check face1
    a=re.findall(r"\d+\.?\d*", arr[face1Number])
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=41),"face1 x0 less than 41"
    assert(x0<=43),"face1 x0 more than 43"
    assert(y0>=83),"face1 y0 less than 83"
    assert(y0<=85),"face1 y0 more than 85"
    assert(x1>=83),"face1 x1 less than 83"
    assert(x1<=85),"face1 x1 more than 85"
    assert(y1>=147),"face1 y1 less than 147"
    assert(y1<=149),"face1 y1 more than 149"
    #check face2
    a=re.findall(r"\d+\.?\d*", arr[face2Number])
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=289),"face2 x0 less than 289"
    assert(x0<=291),"face2 x0 more than 291"
    assert(y0>=101),"face2 y0 less than 101"
    assert(y0<=103),"face2 y0 more than 103"
    assert(x1>=323),"face2 x1 less than 323"
    assert(x1<=325),"face2 x1 more than 325"
    assert(y1>=150),"face2 y1 less than 150"
    assert(y1<=152),"face2 y1 more than 152"
    #check face3
    a=re.findall(r"\d+\.?\d*", arr[face3Number])
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=375),"face3 x0 less than 375"
    assert(x0<=377),"face3 x0 more than 377"
    assert(y0>=50),"face3 y0 less than 50"
    assert(y0<=52),"face3 y0 more than 52"
    assert(x1>=463),"face3 x1 less than 463"
    assert(x1<=465),"face3 x1 more than 465"
    assert(y1>=143),"face3 y1 less than 143"
    assert(y1<=145),"face3 y1 more than 145"

def caffe_wrapper_mtcnn_6faces(targetdir):
    root_dir=targetdir
    target_dir=targetdir+'/build/examples/caffe_wrapper/mtcnn'
    cmd1="export TENGINE_CONFIG_FILE=%s/install/etc/tengine/config"%(root_dir)
    cmd2="echo \"face 0: x0,y0 170.91638 76.79741  x1,y1 208.06985  128.15182\" >> /tmp/master.dummy"
    cmd3="echo \"face 1: x0,y0 104.73532 175.54961  x1,y1 137.31529  236.33575\" >> /tmp/master.dummy"
    cmd4="echo \"face 2: x0,y0 296.50046 183.12787  x1,y1 334.23788  236.24565\" >> /tmp/master.dummy"
    cmd5="echo \"face 3: x0,y0 459.72641 123.38977  x1,y1 506.37677  175.55830\" >> /tmp/master.dummy"
    cmd6="echo \"face 4: x0,y0 66.37959 161.10822  x1,y1 108.99861  243.48486\" >> /tmp/master.dummy"
    cmd7="echo \"face 5: x0,y0 561.20978 199.41609  x1,y1 587.92566  252.88115\" >> /tmp/master.dummy"
    cmd8="echo \"total detected: 6 faces\" >> /tmp/master.dummy"
    cmd=cmd1+"&&"+cmd2+"&&"+cmd3+"&&"+cmd4+"&&"+cmd5+"&&"+cmd6+"&&"+cmd7+"&&"+cmd8
    os.system(cmd)
    target_dir=targetdir+'/build/examples/caffe_wrapper/mtcnn'
    os.popen("cd %s;./CAFFE_MTCNN %s/tests/images/mtcnn_face6.jpg %s/models wrapper_result6.jpg | grep face > /tmp/result.dummy"%(target_dir,root_dir,root_dir),"r")
    line1=os.popen("cat /tmp/master.dummy","r")
    out1=line1.read()
    print(out1)
    line2=os.popen("cat /tmp/result.dummy","r")
    out2=line2.read()
    print(out2)
    assert(out1!=out2)

    arr=out2.splitlines()
    for char in arr:
        if "face 0" in char:
        #find face0 and change the face 0 to list
            char_arr=char.splitlines()
        #index face0Number in arr
            face0Number=arr.index(char_arr[0])
            face1Number=arr.index(char_arr[0])+1
            face2Number=arr.index(char_arr[0])+2
            face3Number=arr.index(char_arr[0])+3

    #check face0
    a=re.findall(r"\d+\.?\d*", arr[face0Number])
    print a
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=168),"face0 x0 less than 168"
    assert(x0<=170),"face0 x0 more than 170"
    assert(y0>=83),"face0 y0 less than 83"
    assert(y0<=85),"face0 y0 more than 85"
    assert(x1>=204),"face0 x1 less than 204"
    assert(x1<=206),"face0 x1 more than 206"
    assert(y1>=133),"face0 y1 less than 133"
    assert(y1<=135),"face0 y1 more than 135"
    #check face1
    a=re.findall(r"\d+\.?\d*", arr[face1Number])
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=41),"face1 x0 less than 41"
    assert(x0<=43),"face1 x0 more than 43"
    assert(y0>=83),"face1 y0 less than 83"
    assert(y0<=85),"face1 y0 more than 85"
    assert(x1>=83),"face1 x1 less than 83"
    assert(x1<=85),"face1 x1 more than 85"
    assert(y1>=147),"face1 y1 less than 147"
    assert(y1<=149),"face1 y1 more than 149"
    #check face2
    a=re.findall(r"\d+\.?\d*", arr[face2Number])
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=289),"face2 x0 less than 289"
    assert(x0<=291),"face2 x0 more than 291"
    assert(y0>=101),"face2 y0 less than 101"
    assert(y0<=103),"face2 y0 more than 103"
    assert(x1>=323),"face2 x1 less than 323"
    assert(x1<=325),"face2 x1 more than 325"
    assert(y1>=150),"face2 y1 less than 150"
    assert(y1<=152),"face2 y1 more than 152"
    #check face3
    a=re.findall(r"\d+\.?\d*", arr[face3Number])
    x0=float(a[3])
    y0=float(a[4])
    x1=float(a[7])
    y1=float(a[8])
    assert(x0>=375),"face3 x0 less than 375"
    assert(x0<=377),"face3 x0 more than 377"
    assert(y0>=50),"face3 y0 less than 50"
    assert(y0<=52),"face3 y0 more than 52"
    assert(x1>=463),"face3 x1 less than 463"
    assert(x1<=465),"face3 x1 more than 465"
    assert(y1>=143),"face3 y1 less than 143"
    assert(y1<=145),"face3 y1 more than 145"

def vgg16_mem(targetdir):
    target_dir=targetdir
    res=os.popen("cd %s; %s/tests/bin/vgg16_mem.sh"%(target_dir,target_dir),"r")
    out=res.read()
    print(out)
    assert "0.4998 - \"n03792782" in out