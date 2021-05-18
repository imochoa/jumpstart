#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'wget' | grep -q "\[installed\]")
then
   echo "[wget] -> [installed!]";
else
   echo "[wget] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'git' | grep -q "\[installed\]")
then
   echo "[git] -> [installed!]";
else
   echo "[git] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


