#!/usr/bin/env bash

sudo apt-get install -y software-properties-common \
&& sudo add-apt-repository -y ppa:andreasbutti/xournalpp-master \
&& sudo apt-get update -y \
&& sudo apt-get install -y xournalpp
