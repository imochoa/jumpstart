#!/usr/bin/env bash

sudo snap install beekeeper-studio

# https://docs.beekeeperstudio.io/installation/#apt-deb
# # Install our GPG key
# wget --quiet -O - https://bintray.com/user/downloadSubjectPublicKey?username=bintray | sudo apt-key add -

# # add our repo to your apt lists directory
# echo "deb https://dl.bintray.com/beekeeper-studio/releases disco main" | sudo tee /etc/apt/sources.list.d/beekeeper-studio.list

# # Update apt and install
# sudo apt update
# sudo apt install beekeeper-studio

# # Installed to '/opt/' by default!
# BEEKEEPER_DIR="/opt/Beekeeper Studio"
# sudo chown -R ${USER}:${USER} "${BEEKEEPER_DIR}"
# sudo rm -f /usr/local/bin/beekeeper-studio
# ln -s ${BEEKEEPER_DIR}/beekeeper-studio /usr/local/bin/beekeeper-studio
# sudo ln -s "${BEEKEEPER_DIR}/beekeeper-studio" /usr/local/bin/beekeeper-studio
