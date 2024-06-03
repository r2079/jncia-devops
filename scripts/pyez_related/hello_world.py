from pprint import pprint 
from jnpr.junos import Device 
import yaml 


with open('/home/ubuntu/scripts/pyez_related/router_data.yml', 'r') as file: 
    data = yaml.safe_load(file)

for router_data in data:
    for device,value in router_data.items():
        host = router_data[device]['host']
        user = router_data[device]['user']
        passwd = router_data[device]['passwd']
        dev = Device(host=host, user=user, passwd=passwd)
        dev.open()
        pprint(dev.facts)
        dev.close()