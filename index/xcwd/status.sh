#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'xcwd' | grep -q "\[installed\]")
then
   echo "[xcwd] -> [installed!]";
else
   echo "[xcwd] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


