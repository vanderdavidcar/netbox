# If you have a sensitive information you must use .gitignore
# Informations below are public 

import pynetbox
import urllib3
urllib3.disable_warnings()

nb_demo_apikey = "fd585028a1668701111f76e447d31baf512e01e4"
nb_demo_user = "admin"
nb_demo_pass = "admin"
nb_demo_url = "https://demo.netbox.dev/"

NETBOX_URL = nb_demo_url
NETBOX_TOKEN = nb_demo_apikey

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False