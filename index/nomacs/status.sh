#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'nomacs' | grep -q "\[installed\]")
then
   echo "[nomacs] -> [installed!]";
else
   echo "[nomacs] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


