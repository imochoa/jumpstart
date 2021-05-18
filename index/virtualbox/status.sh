#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'virtualbox' | grep -q "\[installed\]")
then
   echo "[virtualbox] -> [installed!]";
else
   echo "[virtualbox] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'virtualbox-ext-pack' | grep -q "\[installed\]")
then
   echo "[virtualbox-ext-pack] -> [installed!]";
else
   echo "[virtualbox-ext-pack] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


