#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy entr | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "entr ->  [${V0}]"
