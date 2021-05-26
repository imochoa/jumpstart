#!/usr/bin/env bash

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Clipster
# Config at ~/.config/clipster/clipster.ini

# TODO MOVE TO OPT
mkdir -p ~/Applications \
&& cd ~/Applications \
&& sudo apt install -y python-gi gir1.2-gtk-3.0 git \
&& git clone https://github.com/mrichar1/clipster.git clipster-repo \
&& cp clipster-repo/clipster clipster \
&& rm -rf clipster-repo \
&& sudo ln -s $(realpath clipster) /usr/local/bin/clipster


# Roficlip
# git clone https://github.com/gilbertw1/roficlip.git roficlip-repo
# cp roficlip-repo/roficlip roficlip
# rm -rf roficlip-repo
# sudo ln -s $(realpath roficlip) /usr/bin/roficlip
