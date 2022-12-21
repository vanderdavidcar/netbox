import auth
import re
from napalm import get_network_driver
import json
import urllib3
urllib3.disable_warnings()


with open("devices_3560.txt") as f:
    ios_model = f.read().splitlines()

# NAPALM to get.facts() of IOS
for devices in ios_model:
    driver = get_network_driver("ios")
    device = driver(hostname=devices, username=auth.nb_username, password=auth.nb_password)
    device.open()
    ios_getfacts = json.dumps(device.get_facts(), indent=4)
    print(ios_getfacts)


# Store get.facts() as variable
results = ios_getfacts
print(results)
# Pattern to use regex in a file ios_version.txt
version_pattern = re.compile(r"Version (?P<version>\S..........)")
ios_version = version_pattern.search(results)

# Print regex information collect ina file ios_version.txt
print("IOS Version regex: ".ljust(18) + ios_version.group("version"))
version = ios_version.group("version")

# Retrieve router object for update with dictionary
#for devices in ios_model:
# Update custom fields "sw_version" using regex information collected
devices["custom_fields"]["sw_version"] = version
devices.save()
print("Hostname: ", devices.name)
print("Device Type: ", devices.device_type)
print("sw_version: ", devices.custom_fields["sw_version"])
print("Current tenant: ", devices.tenant)