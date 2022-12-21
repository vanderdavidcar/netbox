# netbox

Netbox using Pynetbox

Project Source of Truth (SoT) using NAPALM to connect on devices to create, update, delete objects in netbox. 

following the instructions below:

## Dependencies: Install the requirements to have all dependencies used

$ pip install -r requirements.txt

## Endpoint

For testing can be used this https://demo.netbox.dev/

## Variables

auth.py
In this file, put all variables you need

## collect_info.py
Is a function to get any information you need based on specific filter

## create_devices_nbdemo.py
Is a function to create devices on netbox via API, it is important to have all ID of fields to specify on code.

## delete_devices_nbdemo.py
Is a function that will looking for devices based on specific filters and according to your answer "yes or not" can remove devices of netbox.