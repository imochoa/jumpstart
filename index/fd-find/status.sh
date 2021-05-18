#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'fd-find' | grep -q "\[installed\]")
then
   echo "[fd-find] -> [installed!]";
else
   echo "[fd-find] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


