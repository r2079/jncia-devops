import os
import textfsm
import jxmlease
from lxml import etree
from jnpr.junos import Device
from jnpr.junos.exception import ConnectError
from jnpr.junos.op import arp
from pprint import pprint

ntc_templates_path = os.path.join(os.path.expanduser("~"), "ntc-templates", "ntc_templates", "templates")

# Lab environment, Use secure methods to authenticate. 
juniper_device = {
    'host': '172.17.0.2',
    'user': 'lab',
    'passwd': 'lab123'}

def get_arp_table(device_params):
    try:
        with Device(**device_params) as dev:
            arp_table = arp.ArpTable(dev)
            arp_table.get()
            output = etree.tostring(arp_table.xml, pretty_print=True).decode()
        return output
    except ConnectError as err:
        print(f"Cannot connect to device: {err}")
        return None

def xml_to_text(xml_str):
    parser = jxmlease.Parser()
    xml_dict = parser(xml_str)
    arp_entries = xml_dict.get("arp-table-information", {}).get("arp-table-entry", [])
    
    lines = ["MAC Address          Address         Interface       Flags"]
    for entry in arp_entries:
        mac_address = entry.get("mac-address", "")
        ip_address = entry.get("ip-address", "")
        interface_name = entry.get("interface-name", "")
        flags = entry.get("flags", "")
        lines.append(f"{mac_address} {ip_address} {interface_name} {flags}")
    
    return "\n".join(lines)

def parse_juniper_output(command_output, command_template):
    template_file = f"{command_template}.textfsm"
    template_path = os.path.join(ntc_templates_path, template_file)
    
    if not os.path.exists(template_path):
        print(f"Template file not found: {template_path}")
        return None
    
    with open(template_path) as template:
        fsm = textfsm.TextFSM(template)
        parsed_result = fsm.ParseText(command_output)
    
    return parsed_result

template_name = "juniper_junos_show_arp_no_resolve_xml"
device_output = get_arp_table(juniper_device)

if device_output:
    text_output = xml_to_text(device_output)
    parsed_data = parse_juniper_output(text_output, template_name)
    if parsed_data:
        pprint(parsed_data)
    else:
        print("Failed to parse the device output.")
else:
    print("Failed to retrieve the device output.")
