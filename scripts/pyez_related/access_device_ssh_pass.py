from jnpr.junos import Device 
from pprint import pprint 
from getpass import getpass 

password = getpass()
dev = Device(host='172.17.0.2', user='vrnetlab', passwd=password)
dev.open()
pprint(dev.facts)
dev.close()
