#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'source-highlight' | grep -q "\[installed\]")
then
   echo "[source-highlight] -> [installed!]";
else
   echo "[source-highlight] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


