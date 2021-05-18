#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'zip' | grep -q "\[installed\]")
then
   echo "[zip] -> [installed!]";
else
   echo "[zip] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'unzi' | grep -q "\[installed\]")
then
   echo "[unzi] -> [installed!]";
else
   echo "[unzi] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


