#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy vim | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "vim ->  [${V0}]"
V1=$(apt-cache policy vim-gtk | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "vim-gtk ->  [${V1}]"
V2=$(apt-cache policy vim-tiny | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "vim-tiny ->  [${V2}]"