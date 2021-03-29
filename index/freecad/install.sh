#!/usr/bin/env bash

sudo apt-get install -y software-properties-common
sudo add-apt-repository -y ppa:freecad-maintainers/freecad-stable
sudo apt-get update -y
sudo apt-get install -y freecad freecad-common freecad-python3

# Default to using py3! (TODO Does this work?)
# sudo update-alternatives --config freecad
