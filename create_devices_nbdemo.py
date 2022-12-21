import auth

# Vendors
model = ["catalyst","c9200","c9300"]

def add_dev():
    for vendors in model:
        # Using hostnames in an external file
        with open(f"devices_{vendors}.txt") as f:
            ios_model = f.read().splitlines()
            print(ios_model)

        for devices in ios_model:
            results = auth.nb.dcim.devices.create(
                    name=devices,
                    device_type=2,
                    device_role=1,
                    tenant=9,
                    manufacturer=3,
                    site=1,
            )
            print(f'\nDevice created: {results}')
add_dev()