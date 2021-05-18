#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'p7zip-full' | grep -q "\[installed\]")
then
   echo "[p7zip-full] -> [installed!]";
else
   echo "[p7zip-full] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


