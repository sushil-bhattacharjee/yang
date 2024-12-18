from scrapli_netconf import NetconfDriver

my_device = {
    "host": "10.1.10.11",
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
    "port": 830
}

ospf_filter = """
<ospf-oper-data xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-ospf-oper">
</ospf-oper-data>
"""

try:
    conn = NetconfDriver(**my_device)
    conn.open()
    response = conn.get(filter_=ospf_filter, filter_type="subtree")
    print(response.result)
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    conn.close()
