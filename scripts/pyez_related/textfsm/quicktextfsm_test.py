from jnpr.junos import Device
import textfsm
from pprint import pprint 

# This is a lab environment, for prod use secure methods 
device_args = {"host":"172.17.0.2","user":"lab","passwd":"lab123"}

with Device(**device_args) as dev:
    output = dev.cli("show arp no-resolve",format="text")

template = "/home/ubuntu/ntc-templates/ntc_templates/templates/juniper_junos_show_arp_no-resolve.textfsm"

with open(template) as t:
    fsm = textfsm.TextFSM(t)
    parsed_output = fsm.ParseText(output)
    pprint(parsed_output)