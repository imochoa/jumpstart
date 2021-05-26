#!/usr/bin/env bash

sudo apt install -y software-properties-common \
&& sudo add-apt-repository -y ppa:andreasbutti/xournalpp-master \
&& sudo apt update -y \
&& sudo apt install -y xournalpp
