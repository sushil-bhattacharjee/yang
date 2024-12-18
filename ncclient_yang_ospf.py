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
ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
    <ospf-state>
        <ospf-instance>
            <af>address-family-ipv4</af>
            <router-id>16843009</router-id>
                <ospf-area>
                    <area-id>0</area-id>
                    <ospf-interface>
                        <name>GigabitEthernet3</name>
                            <ospf-neighbor>
                                <neighbor-id>3.3.3.3</neighbor-id>
                                    <state></state>
                            </ospf-neighbor>
                    </ospf-interface>
                </ospf-area>
        </ospf-instance>
    </ospf-state>
</ospf-oper-data>
"""

try:
    with manager.connect(**device) as m:
        # Use raw filter without <filter> if supported by the server
        response = m.get(('subtree', ospf_filter))

        # Parse the XML and pretty-print it
        xml_response = parseString(response.xml)
        pretty_xml = xml_response.toprettyxml(indent="  ")

        # Print the formatted XML
        print(pretty_xml)
except Exception as e:
    print(f"An error occurred: {e}")


