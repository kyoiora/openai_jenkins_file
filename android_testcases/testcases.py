
import argparse
import pdb
import sys
print sys.path
#pdb.set_trace()
from adb_wrapper.adb_wrapper.adb_wrapper import AdbWrapper
ROOT_DIR='/root/tengine_armv8/android_pack/'
TARGET_DIR_ON_BOARD='/data/local/tmp/'


def push():

    a = AdbWrapper() # Auto Find adb in system PATH or Environment
    a.connect(android_ip)
    #pdb.set_trace()
    a.device=android_ip
    a.push(ROOT_DIR, TARGET_DIR_ON_BOARD)
    res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
    print(res[0])
    res=a.shell("cd %s && chmod u+x Classify "%(TARGET_DIR_ON_BOARD+'android_pack/'))

    res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))

    #pdb.set_trace()
    print(res[0])



def Classify1(android_ip):
	target_dir=TARGET_DIR_ON_BOARD+'android_pack/'
	a = AdbWrapper() # Auto Find adb in system PATH or Environment
	a.connect(android_ip)
	#pdb.set_trace()
	a.device=android_ip

	a.shell("export LD_LIBRARY_PATH=%s"%target_dir)
	#res=a.shell("ls -al %s"%(TARGET_DIR_ON_BOARD+'android_pack/'))
	#print(res[0])
	#res=a.shell("\'cd %s &&  ./Classify -i cat.jpg \'"%(TARGET_DIR_ON_BOARD+'android_pack/'))
	res=a.shell("export LD_LIBRARY_PATH=%s; %s/Classify -i %s/cat.jpg "%(target_dir,target_dir,target_dir))
	#pdb.set_trace()
	print(res)

def Classify2(android_ip):
	pass