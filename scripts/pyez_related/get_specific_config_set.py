
from jnpr.junos import Device 
from lxml import etree


with Device(host='172.17.0.2',user='vrnetlab',passwd='VR-netlab9') as dev: 
    filter = '<configuration><protocols><bgp></bgp></protocols></configuration>'
    configuration = dev.rpc.get_config(filter_xml=filter, options={'format':'set'})
    config_after_lxml = etree.tostring(configuration, encoding='unicode')
    final_config = config_after_lxml.replace('<configuration-set>',' ').replace('</configuration-set>', ' ')
    print(final_config)