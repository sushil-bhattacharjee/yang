from ncclient import manager
from xml.dom.minidom import parseString
from rich import print

# Device connection details
device = {
    "host": "10.1.10.11",
    "port": 830,
    "username": "cisco",
    "password": "cisco",
    "hostkey_verify": False
}

# Corrected NETCONF filter without <filter> wrapper

neighbor_state_std = '/ospf-oper-data/ospf-state/ospf-instance[af="address-family-ipv4" and router-id="16843009"]/ospf-area[area-id=0]/ospf-interface[name="GigabitEthernet3"]/ospf-neighbor[neighbor-id="3.3.3.3"]/state'
neighbor_state = '//ospf-neighbor[neighbor-id="3.3.3.3"]/state'
try:
    with manager.connect(**device) as m:
        # Use raw filter without <filter> if supported by the server
        response = m.get(('xpath', neighbor_state))

        # Parse the XML and pretty-print it
        xml_response = parseString(response.xml) 
        pretty_xml = xml_response.toprettyxml(indent="  ")

        # Print the formatted XML
        print(pretty_xml)
except Exception as e:
    print(f"An error occurred: {e}")
