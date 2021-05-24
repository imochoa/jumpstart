
# https://www.arduino.cc/en/guide/linux
# https://snapcraft.io/arduino
echo "https://www.arduino.cc/en/guide/linux"
echo "In order to use the serial port to upload sketches ";
echo "the current user needs to be added to the dialout group. ";
echo "The changes will take effect after logging out and back in";

sudo usermod -a -G dialout $USER

