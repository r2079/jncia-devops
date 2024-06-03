"""
This script is to delete the docker containers and re-add them. 
"""

import os 
import time 

os.system("sudo docker rm -f vmx1")
os.system("sudo docker rm -f vmx2")
os.system("sudo docker rm -f vr-xcon")
print("\n-> Removed previous vmx1/2/vr-xcon")
print("-> Spinning up new vmx1/vmx2/vr-xcon")
print("\n")
os.system("sudo docker run -d --privileged --name vmx1 432ba9e1fc79")
os.system("sudo docker run -d --privileged --name vmx2 432ba9e1fc79")
os.system("sudo docker run -d --privileged --name vr-xcon --link vmx1 --link vmx2 78a5a1b769f0 --p2p vmx1/2--vmx2/2 vmx1/3--vmx2/3")
print("\n-> Done with Spin! Should be available in sometime!")


