#!/usr/bin/python

# This script assumes that the Shelly device is already connected to the ICG's
# Wifi AP.  It now will check for OTA updates and setup MQTT
# The script takes a single argument of the Shelly's IP address

# https://shelly-api-docs.shelly.cloud/#common-http-api

import requests
import json
import sys
from time import sleep


def run_config(ip):

    desired = {"mqtt_un": "",
               "mqtt_pw": ""}

    # connect and get device info
    print "*****  DEVICE INFO  *****"
    r = requests.get('http://%s/shelly' % (ip,))
    print json.dumps(r.json())

    print "*****  INITIAL CONFIG  *****"
    r = requests.get('http://%s/settings' % (ip,))
    print json.dumps(r.json())


    # Step 2 - Check for OTA update and perform
    print "*****  OTA  *****"
    # Enable Shelly Cloud interface
    r = requests.post('http://%s/settings/cloud' % (ip,), {'enabled':True})
    print r

    r = requests.get('http://%s/ota' % (ip,))
    print r.json()

    if r.json().get('has_update'):
        print "Executing OTA..."
        r = requests.post('http://%s/ota' % (ip,), {'update': True})

        while True:
            sleep(2)
            r = requests.get('http://%s/ota' % (ip,))
            print r.json()
            if r.json().get('has_update') is False:
                break

    # Step 3 - setup MQTT parameters
    print "*****  CONFIGURING DEVICE  *****"
    params = {'mqtt_enable':        True,
              'mqtt_server':        '192.168.10.1:1884',
              'mqtt_user':          desired.get('mqtt_un'),
              'mqtt_pass':          desired.get('mqtt_pw'),
              'mqtt_clean_session': True,
              'mqtt_retain':        True
              }
    r = requests.post('http://%s/settings' % (ip,), params)
    print r

    # Disable SNTP
    r = requests.post('http://%s/settings' % (ip,), {'sntp_server': ''})
    print r

    # Disable Shelly Cloud interface
    r = requests.post('http://%s/settings/cloud' % (ip,), {'enabled': False})
    print r

    print "*****  FINAL SETTINGS  *****"
    r = requests.get('http://%s/settings' % (ip,))
    print json.dumps(r.json())

    # Reboot the device
    print "*****  REBOOTING  *****"
    r = requests.post('http://%s/reboot' % (ip,))
    print r


def main():
    # print command line arguments
    ip = sys.argv[1]
    print "Configuring Shelly device at %s..." % (ip,)
    run_config(ip)


if __name__ == "__main__":
    main()
