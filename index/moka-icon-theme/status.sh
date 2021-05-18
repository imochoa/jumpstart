#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'moka-icon-theme' | grep -q "\[installed\]")
then
   echo "[moka-icon-theme] -> [installed!]";
else
   echo "[moka-icon-theme] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


