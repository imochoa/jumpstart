#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'python-gi' | grep -q "\[installed\]")
then
   echo "[python-gi] -> [installed!]";
else
   echo "[python-gi] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'gir1' | grep -q "\[installed\]")
then
   echo "[gir1] -> [installed!]";
else
   echo "[gir1] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


