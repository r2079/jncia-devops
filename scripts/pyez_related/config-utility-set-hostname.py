# set the hostname to vmx-100 and just print the diff 

from jnpr.junos import Device 
from jnpr.junos.utils.config import Config
from lxml import etree

config_xml = etree.XML('<configuration><system><host-name>vmx0</host-name></system></configuration>')
with Device(host='172.17.0.2',user='vrnetlab',passwd='VR-netlab9') as dev:
    with Config(dev, mode="exclusive") as cu:
        cu.load(config_xml, format="xml")
        print(cu.pdiff())
