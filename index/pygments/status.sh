#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'python3-pygments' | grep -q "\[installed\]")
then
   echo "[python3-pygments] -> [installed!]";
else
   echo "[python3-pygments] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


