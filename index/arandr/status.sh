#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'arandr' | grep -q "\[installed\]")
then
   echo "[arandr] -> [installed!]";
else
   echo "[arandr] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


