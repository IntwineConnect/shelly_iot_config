# shelly_iot_config
Script collection using the Shelly REST APIs to configure them for Intwine IoT applications

Intwine enables integration between Shelly[1] devices and the Intwine Connected Gateway (ICG). The scripts contained in this project are provided to help configure the Shelly devices to connect to the ICG's MQTT broker.

Shelly provides API over both REST and MQTT [2].  These scripts utilize the REST API to do the following:

shelly_setup_wifi.py:
  * run this when connected to the Wifi AP hosted by the Shelly device
  * the script will configure the Shelly device to connect to the ICG's builtin Wifi AP
  * the script will configure the Shelly with a specified static IP address.  This helps to reduce battery use

shelly_config.py:
  * this script is run on the ICG itself after the Shelly has been connected
  * It will print the original settings
  * check for, and if available perform, a firmware update of the device
  * configure the device to connect to the ICG's MQTT broker
  * disable SNTP (to reduce battery use)
  * disable the Shelly cloud interface (to minimize cellular data use)
  * print the final settings
  * reboot the device

[1] https://shelly.cloud/
[2] https://shelly-api-docs.shelly.cloud/#common-http-api
