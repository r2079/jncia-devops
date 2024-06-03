# set the hostname to vmx-100 and just print the diff 

from jnpr.junos import Device 
from jnpr.junos.utils.config import Config
from lxml import etree

with Device(host='172.17.0.2',user='vrnetlab',passwd='VR-netlab9') as dev:
    with Config(dev, mode="exclusive") as cu:
        cu.load('/home/ubuntu/scripts/pyez_related/load-patch.diff', format="conf",patch=True,ignore_warning='ignoring noise in patch:')
        cu.pdiff()

