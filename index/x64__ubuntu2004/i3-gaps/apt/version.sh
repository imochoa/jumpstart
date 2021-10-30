#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy arandr | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "arandr ->  [${V0}]"
V1=$(apt-cache policy compton | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "compton ->  [${V1}]"
V2=$(apt-cache policy feh | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "feh ->  [${V2}]"
V3=$(apt-cache policy fonts-source-code-pro-ttf | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "fonts-source-code-pro-ttf ->  [${V3}]"
V4=$(apt-cache policy htop | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "htop ->  [${V4}]"
V5=$(apt-cache policy i3-gaps | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "i3-gaps ->  [${V5}]"
V6=$(apt-cache policy i3-gaps-wm | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "i3-gaps-wm ->  [${V6}]"
V7=$(apt-cache policy i3-snapshot | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "i3-snapshot ->  [${V7}]"
V8=$(apt-cache policy i3blocks | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "i3blocks ->  [${V8}]"
V9=$(apt-cache policy lxappearance | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "lxappearance ->  [${V9}]"
V10=$(apt-cache policy moka-icon-theme | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "moka-icon-theme ->  [${V10}]"
V11=$(apt-cache policy nordic | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "nordic ->  [${V11}]"
V12=$(apt-cache policy rofi | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "rofi ->  [${V12}]"
V13=$(apt-cache policy xbacklight | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "xbacklight ->  [${V13}]"
