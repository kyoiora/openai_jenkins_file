
import argparse
import pdb
import sys
TARGET_DIR_ON_BOARD='/home/rk/tengine/examples/imagenet_classification'

def imagenet_sqz():
    target_dir=TARGET_DIR_ON_BOARD
    res=shell("cd %s;export LD_LIBRARY_PATH=%s; %s/Classify -n squeezenet "%(target_dir,target_dir,target_dir))
    print(res[0])
    assert "0.2763 - \"n02123045" in res[0]
    imagenet_sqz()