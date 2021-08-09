#!/usr/bin/env sh

# DO NOT MODIFY!
# THIS FILE WAS AUTOGENERATED BY *generate-status-files.py*

missing=0;


if $(apt list --installed 'fonts-font-awesome' | grep -q "\[installed\]")
then
   echo "[fonts-font-awesome] -> [installed!]";
else
   echo "[fonts-font-awesome] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'fonts-noto-color-emoji' | grep -q "\[installed\]")
then
   echo "[fonts-noto-color-emoji] -> [installed!]";
else
   echo "[fonts-noto-color-emoji] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi
