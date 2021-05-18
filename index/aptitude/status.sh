#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'aptitude' | grep -q "\[installed\]")
then
   echo "[aptitude] -> [installed!]";
else
   echo "[aptitude] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


