from scrapli_netconf import NetconfDriver

# Device connection details
device = {
    "host": "10.1.10.11",
    "port": 830,
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
}

# Example filter for getting specific data
ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper"  xmlns:ospf-ios-xe-oper="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
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
    # Initialize and open the NetconfDriver connection
    conn = NetconfDriver(**device)
    conn.open()

    # Fetch data using the `get` function with a filter
    response = conn.get(filter_=ospf_filter, filter_type="subtree")
    
    # Print the raw XML response
    print("Response from the get() function:")
    print(response.result)

    # Close the connection
    conn.close()

except Exception as e:
    print(f"An error occurred: {e}")
    
#####This code doesn't work #####################

