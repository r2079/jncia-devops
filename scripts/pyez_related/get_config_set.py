# To get set based configuration from the device, we need to use RPC. 

from jnpr.junos import Device 
from lxml import etree

with Device(host='172.17.0.2',user='vrnetlab',passwd='VR-netlab9') as dev: 
    configuration = dev.rpc.get_config(options={'format':'set'})
    config_after_lxml = etree.tostring(configuration, encoding='unicode')
    print(config_after_lxml)