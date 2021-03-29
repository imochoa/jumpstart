#!/usr/bin/env bash
sudo apt install -y git \
&& sudo mkdir -p /opt/ \
&& cd /opt/ \
&& sudo git clone https://github.com/schischi/xcwd.git xcwd \
&& sudo chown -R ${USER}:${USER} /opt/xcwd \
&& cd xcwd/ \
&& make \
&& sudo checkinstall
# && sudo make install
