#!/usr/bin/env bash
sudo add-apt-repository --remove ppa:bashtop-monitor/bashtop \
&& sudo apt update -y \
&& sudo apt remove -y bashtop
