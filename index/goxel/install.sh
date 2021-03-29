#!/usr/bin/env bash

sudo apt install -y scons pkg-config libglfw3-dev libgtk-3-dev git \
&& cd /opt/ \
&& git clone https://github.com/guillaumechereau/goxel goxel \
&& cd goxel \
&& make release \
&& sudo ln -s /opt/goxel/goxel /usr/local/bin/goxel
