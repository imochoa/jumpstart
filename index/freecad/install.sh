#!/usr/bin/env bash

sudo apt install -y software-properties-common
sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
sudo apt update -y
sudo apt install -y freecad freecad-common freecad-python3

# Default to using py3! (TODO Does this work?)
# sudo update-alternatives --config freecad
