#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

V0=$(apt-cache policy texlive-fonts-extra | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "texlive-fonts-extra ->  [${V0}]"
V1=$(apt-cache policy texlive-full | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "texlive-full ->  [${V1}]"
V2=$(apt-cache policy texlive-latex-extra | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "texlive-latex-extra ->  [${V2}]"
V3=$(apt-cache policy texlive-xetex | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "texlive-xetex ->  [${V3}]"
V4=$(apt-cache policy texstudio | grep Candidate: | rev | cut -d: -f1 | rev | cut -d- -f1)
echo "texstudio ->  [${V4}]"