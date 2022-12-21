# netbox-automation

Netbox using Pynetbox

Project Source of Truth (SoT) using NAPALM to connect on devices to create, update, delete objects in netbox. 

following the instructions below:

## Dependencies: Install the requirements to have all dependencies used

$ pip install -r requirements.txt

## Endpoint

For testing can be used this https://demo.netbox.dev/

## Variables

config_vars.py
In this file, put on variables you need and import in each file .py that using credentials.

Token API take on netbox
api_key = "XXXXXX"

Create a username and pasword
nb_username = "netbox"
nb_password = "XXXXXXXXX"
nb_url = "https://demo.netbox.dev/"

## Authentication method

Put api token, URL, username and password informations into variables in config.py file.

## IP/FQDN - DNS

I am using WSL (Windows Subsystem Linux) to tests all codes, so access by SSH was done with FQDN, all devices needed into /etc/hosts, so if you prefer using IP address to connect on devices

To avoid the error below, please make sure you have a DNS of devices in /etc/hosts

raise NetmikoTimeoutException(msg)
netmiko.ssh_exception.NetmikoTimeoutException: DNS failure--the hostname you provided was not resolvable in DNS: dmi01-akron-rtr01:22

## Netmiko and NAPALM information

There are many files .py split by device version, so I'm  using Netmiko to connect on devices and update certain fields on Netbox, however to stay up-to-date I am using NAPALM too, in this way I have a Source of Truth (SoT)