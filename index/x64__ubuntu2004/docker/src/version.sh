#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy docker.io | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "docker.io ->  [${V0}]"