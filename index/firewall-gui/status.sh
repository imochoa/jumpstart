#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'gufw' | grep -q "\[installed\]")
then
   echo "[gufw] -> [installed!]";
else
   echo "[gufw] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


