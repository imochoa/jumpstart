#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'default-jre' | grep -q "\[installed\]")
then
   echo "[default-jre] -> [installed!]";
else
   echo "[default-jre] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


