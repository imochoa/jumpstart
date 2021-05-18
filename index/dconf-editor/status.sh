#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'dconf-editor' | grep -q "\[installed\]")
then
   echo "[dconf-editor] -> [installed!]";
else
   echo "[dconf-editor] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


