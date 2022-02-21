#!/usr/bin/env bash

# https://www.arduino.cc/en/guide/linux
# https://snapcraft.io/arduino
echo -e "https://www.arduino.cc/en/guide/linux"
echo -e "In order to use the serial port to upload sketches ";
echo -e "the current user needs to be added to the dialout group. ";
echo -e "The changes will take effect after logging out and back in";

sudo usermod -a -G dialout $USER
echo -e  "Reboot your computer to take effect!"

echo -e "The snap install's python interpreter is isolated from your default system one"
echo -e "If it complains about missing packages, you might have to run something like:"
echo -e ">>>>>>>>>>  arduino.pip install requests"


ESP_SETUP_URL='http://www.martyncurrey.com/esp8266-and-the-arduino-ide/#ESP8266_Basic_Specs'
echo -e "For a guide on setting up the ESP8266"
echo -e ">>>>>>>>>>  ${ESP_SETUP_URL}"
echo -e ""

ESP_BOARD_JSON='http://arduino.esp8266.com/stable/package_esp8266com_index.json'
echo -e "For Adding the board to the arduino ide:"
echo -e ">>>>>>>>>> File > Preferences > Settings > Additional Board Manager URLs"
echo -e ">>>>>>>>>>  ${ESP_BOARD_JSON}"
echo -e ">>>>>>>>>>  Now go to the Boards Manager and install the 'esp8266'"
echo -e ">>>>>>>>>> Tools > Boards > Boards Manager > esp8266"
echo -e ""

ESP_WIFI_URL='http://www.martyncurrey.com/esp8266-and-the-arduino-ide-part-5-adding-wifimanager/'
echo -e "For using WiFi follow:"
echo -e ">>>>>>>>>>  ${ESP_WIFI_URL}"
echo -e ""

WIFIMANAGER_URL='https://github.com/khoih-prog/ESP_WiFiManager'
WIFIMANAGER_GUIDE='https://www.ardu-badge.com/ESP_WiFiManager'
echo -e "You'll need the WifiManager Library"
echo -e "There are different versions. Here's a good one for the ESP8266:"
echo -e ">>>>>>>>>> SOURCE:  ${WIFIMANAGER_URL}"
echo -e ">>>>>>>>>> GUIDE:   ${WIFIMANAGER_GUIDE}"
echo -e ">>>>>>>>>> Tools > Manage Libraries > esp8266"
echo -e ""
