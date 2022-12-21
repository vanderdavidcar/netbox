import auth

def delete_dev():
    # List all devices found
    list_obj = list(auth.nb.dcim.devices.filter(device_type="mx80"))
    print(f'\nList of devices can be removed from Netbox:\n\n {list_obj}')

    obj_input = input("\nPlease input yes or no: \n")
    
    if obj_input == "yes": 
        print('All devices above will be removed of Netbox')
        del_obj = auth.nb.dcim.devices.filter(device_type="mx80")
        del_obj.delete()
    
    elif obj_input == "no":
        print("All devices above will be not removed")

    
delete_dev()