#!/usr/bin/env bash
# TODO FONTS NOT FOUND:
# -- Font not found: fixed:pixelsize=10
# -- Font not found: unifont:fontformat=truetype
# -- Font not found: siji:pixelsize=10

# -- Trying to enable ccache
# -- Couldn't locate ccache, disabling ccache...

# Deps
sudo apt install -y build-essential git cmake cmake-data pkg-config python3-sphinx libcairo2-dev libxcb1-dev libxcb-util0-dev libxcb-randr0-dev libxcb-composite0-dev python3-xcbgen xcb-proto libxcb-image0-dev libxcb-ewmh-dev libxcb-icccm4-dev

# optional deps
sudo apt install -y libxcb-xkb-dev libxcb-xrm-dev libxcb-cursor-dev libasound2-dev libpulse-dev libjsoncpp-dev libmpdclient-dev libcurl4-openssl-dev libnl-genl-3-dev

# i3-wm  # REMOVED it!

cd /opt
sudo git clone --recursive https://github.com/polybar/polybar.git polybar
sudo chown -R ${USER}:${USER} /opt/polybar

cd polybar
# Get new tags from remote
git fetch --tags
# Get latest tag name
latestTag=$(git describe --tags `git rev-list --tags --max-count=1`)

# Checkout latest tag
git checkout $latestTag
 ./build.sh --all-features --gcc -f --install-config --auto
