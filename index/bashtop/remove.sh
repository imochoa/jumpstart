#!/usr/bin/env bash
sudo add-apt-repository --remove ppa:bashtop-monitor/bashtop \
&& sudo apt-get update -y \
&& sudo apt remove -y bashtop
