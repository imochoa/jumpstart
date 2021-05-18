#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'xclip' | grep -q "\[installed\]")
then
   echo "[xclip] -> [installed!]";
else
   echo "[xclip] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


