#!/usr/bin/env sh
missing=0;

if $(snap list | cut -f1 -d' ' | tail -n +2 | grep -q 'beekeeper-studio')
then
   echo "[beekeeper-studio] -> [installed!]";
else
   echo "[beekeeper-studio] -> [NOT installed!]";
   exit 1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi

