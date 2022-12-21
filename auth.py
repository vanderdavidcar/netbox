# .gitignore should include reference to config.py
import pynetbox
import urllib3
urllib3.disable_warnings()

nb_demo_apikey = "14dfa057d9a7779bed35afb878674f0c2e3b310d"
nb_demo_user = "admin"
nb_demo_pass = "admin"
nb_demo_url = "https://demo.netbox.dev/"

NETBOX_URL = nb_demo_url
NETBOX_TOKEN = nb_demo_apikey

nb = pynetbox.api(url=NETBOX_URL, token=NETBOX_TOKEN)
nb.http_session.verify = False