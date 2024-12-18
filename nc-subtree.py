from scrapli_netconf import NetconfDriver


my_device = {
    "host": "10.1.10.11",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830
}

# conn = NetconfDriver(**my_device)
# conn.open()

# ospf_filter = """
# <ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
# </ospf-oper-data>
# """

# response = conn.get(filter_=ospf_filter, filter_type='subtree')
# print(response.result)


# from scrapli_netconf.driver import NetconDriver


ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
    <ospf-state>        
        <ospf-instance>
          <af>address-family-ipv4</af>
          <router-id>16843009</router-id>
          <ospf-area>
            <area-id>0</area-id>
              <ospf-interface>
               <name>Loopback0</name>
               <passive></passive>
              </ospf-interface>
            </ospf-area>
        </ospf-instance>
    </ospf-state>
</ospf-oper-data>
"""

conn = NetconfDriver(**my_device)
conn.open()
response = conn.get(
    filter_=ospf_filter, filter_type='subtree')
print(response.result)