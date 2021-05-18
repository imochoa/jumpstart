#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'software-properties-common' | grep -q "\[installed\]")
then
   echo "[software-properties-common] -> [installed!]";
else
   echo "[software-properties-common] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


