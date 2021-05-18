#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'anki' | grep -q "\[installed\]")
then
   echo "[anki] -> [installed!]";
else
   echo "[anki] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


