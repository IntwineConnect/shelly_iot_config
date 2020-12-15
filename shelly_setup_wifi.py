# Connect to the Shelly Wifi AP and change it to connect to the ICG's Wifi AP
# using the desired static IP address

# https://shelly-api-docs.shelly.cloud/#common-http-api

import requests
import json

desired = {"ip":      "",
           "iguid":   ""}


IP = 'http://192.168.33.1'

# connect and get device info
print "*****  DEVICE INFO  *****"
r = requests.get('%s/shelly' % (IP,))
print json.dumps(r.json())


# change Wifi settings to connect to ICG
print "*****  CONFIGURING AS WIFI CLIENT  *****"
params = {'enabled': True,
          'ssid':    'intwine-icg-%s' % (desired.get('iguid')[0:4],),
          'key':     desired.get('iguid')[8:],
          'ipv4_method': 'static',
          'ip':      desired.get('ip'),
          'netmask': '255.255.255.0',
          'gateway': '192.168.10.1',
          'dns':     '192.168.10.1'
          }
r = requests.post('%s/settings/sta' % (IP,), params)
print r
