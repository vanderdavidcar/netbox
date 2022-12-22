#!/usr/bin/env python
import auth

def collect_info():
    #status_cond = list(nb.dcim.devices.filter(tenant="connect-edge", status="active"))
    status_cond = list(auth.nb.dcim.devices.filter(device_type="mx80"))
    for i in status_cond:
        if i:
            print(" ")
            print("Hostname:        ", i.name)
            print("IP address:      ", i.primary_ip)
            print("Netbox tenant:   ", i.tenant)
            print("sw_version:      ", i.custom_fields["sw_version"])
            print("Model:           ", i.device_type["model"])
            print("Serial Number:   ", i.serial)
            print("Vendor:          ", i.device_type["manufacturer"]["display"])
            print("Site:            ", i.site)
            print("Region:          ", i.location)
            print("Asset Tag:       ", i.asset_tag)
            print(" ")

collect_info()