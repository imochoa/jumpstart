#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'dmenu' | grep -q "\[installed\]")
then
   echo "[dmenu] -> [installed!]";
else
   echo "[dmenu] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


