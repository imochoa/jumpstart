#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy fzf | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "fzf ->  [${V0}]"