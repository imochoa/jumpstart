#!/bin/bash

# clean up dir

URL="https://www.mozilla.org/en-US/firefox/download/thanks/"
wget

tar xjf firefox-*.tar.bz2

mv firefox /opt

# Use `install` instead?
ln -s /opt/firefox/firefox /usr/local/bin/firefox

# Download a copy of the desktop file
wget https://raw.githubusercontent.com/mozilla/sumo-kb/main/install-firefox-linux/firefox.desktop -P /usr/local/share/applications


# Requirements
# https://www.mozilla.org/en-US/firefox/112.0.1/system-requirements/
Firefox will not run at all without the following libraries or packages:
glibc 2.17 or higher
GTK+ 3.14 or higher
libstdc++ 4.8.1 or higher
X.Org 1.0 or higher (1.7 or higher is recommended)
For optimal functionality, we recommend the following libraries or packages:
DBus 1.0 or higher
GNOME 2.16 or higher
libxtst 1.2.3 or higher
NetworkManager 0.7 or higher
PulseAudio
