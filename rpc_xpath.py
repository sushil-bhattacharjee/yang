from ncclient import manager
# trunk-ignore(bandit/B408)
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

# Corrected NETCONF RPC Filter
rpc_filter = '''
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter xmlns:t="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper" type="xpath" 
      select="/t:ospf-oper-data/t:ospf-state/t:ospf-instance[t:af='address-family-ipv4' and t:router-id='16843009']/t:ospf-area[t:area-id='0']/t:ospf-interface[t:name='GigabitEthernet3']/t:ospf-neighbor[t:neighbor-id='3.3.3.3']/t:state" />
    </filter>
  </get>
</rpc>
'''

try:
    with manager.connect(**device) as m:
        # Use raw filter with RPC
        response = m.dispatch(rpc_filter)

        # Parse the XML and pretty-print it
        # trunk-ignore(bandit/B318)
        xml_response = parseString(response.xml)
        pretty_xml = xml_response.toprettyxml(indent="  ")

        # Print the formatted XML
        print(pretty_xml)
except Exception as e:
    print(f"An error occurred: {e}")

