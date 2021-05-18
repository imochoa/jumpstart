#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'trash-cli' | grep -q "\[installed\]")
then
   echo "[trash-cli] -> [installed!]";
else
   echo "[trash-cli] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


