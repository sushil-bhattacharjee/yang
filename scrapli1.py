from scrapli_netconf import NetconfDriver

# Device connection details
device = {
    "host": "10.1.10.11",
    "port": 830,
    "auth_username": "cisco",
    "auth_password": "cisco",
    "auth_strict_key": False,
}

try:
    # Initialize and open the NetconfDriver connection
    conn = NetconfDriver(**device)
    conn.open()

    # Fetch device capabilities
    capabilities = conn.server_capabilities

    # Print the capabilities to verify the connection
    print("NETCONF Capabilities:")
    for capability in capabilities:
        print(capability)

    # Close the connection
    conn.close()

except Exception as e:
    print(f"An error occurred: {e}")
