#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'ripgrep' | grep -q "\[installed\]")
then
   echo "[ripgrep] -> [installed!]";
else
   echo "[ripgrep] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


