#!/usr/bin/env sh

# DO NOT MODIFY!
# THIS FILE WAS AUTOGENERATED BY *generate-status-files.py*

missing=0;


if $(apt list --installed 'openssh-server' | grep -q "\[installed\]")
then
   echo "[openssh-server] -> [installed!]";
else
   echo "[openssh-server] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'xclip' | grep -q "\[installed\]")
then
   echo "[xclip] -> [installed!]";
else
   echo "[xclip] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'xauth' | grep -q "\[installed\]")
then
   echo "[xauth] -> [installed!]";
else
   echo "[xauth] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi

