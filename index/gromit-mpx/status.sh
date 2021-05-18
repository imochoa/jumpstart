#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'gromit-mpx' | grep -q "\[installed\]")
then
   echo "[gromit-mpx] -> [installed!]";
else
   echo "[gromit-mpx] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


