#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy clamav | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "clamav ->  [${V0}]"
V1=$(apt-cache policy clamav-daemon | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "clamav-daemon ->  [${V1}]"
