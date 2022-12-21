import auth

# Vendors
model = ["catalyst","c9200","c9300"]

def update_cust_fields():
    # List all devices found
    list_obj = list(auth.nb.dcim.devices.filter(device_type="mx80"))
    print(f'\nList of devices will be updated:\n\n {list_obj}')

    for vendors in model:
        # Using hostnames in an external file
        with open(f"devices_{vendors}.txt") as f:
            ios_model = f.read().splitlines()
        
        for devices in ios_model:

            # Update custom fields "sw_version" using regex information collected
            devices.custom_fields["sw_version"] = "none"
            devices.save()
            print("Hostname: ", devices.name)
            print("Device Type: ", devices.device_type)
            print("sw_version: ", devices.custom_fields["sw_version"])
            print("Current tenant: ", devices.tenant)

update_cust_fields()