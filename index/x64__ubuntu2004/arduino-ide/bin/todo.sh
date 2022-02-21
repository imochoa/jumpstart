#!/usr/bin/env sh

Ubuntu tar install:
https://ubuntu.com/tutorials/install-the-arduino-ide#2-installing-via-a-tarball

https://downloads.arduino.cc/arduino-1.8.13-linuxaarch64.tar.xz

# Get latest release
https://github.com/arduino/Arduino/releases


# Set up install

# The Arduino IDE will not be able to upload programs to boards because this user (imochoa) does not have permission to access USB boards. To fix this, please open a terminal and run the following command.

sudo usermod -a -G dialout "${USER}"

echo "Reboot your computer!"


https://www.arduino.cc/en/Guide
