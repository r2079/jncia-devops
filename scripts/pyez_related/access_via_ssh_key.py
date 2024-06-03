from jnpr.junos import Device 
from pprint import pprint 
dev = Device(host='172.17.0.2', user='lab', ssh_private_key_file='/home/ubuntu/.ssh/vmx1')
dev.open()
pprint(dev.facts)
dev.close()
