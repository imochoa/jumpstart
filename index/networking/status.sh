#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'wget' | grep -q "\[installed\]")
then
   echo "[wget] -> [installed!]";
else
   echo "[wget] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'curl' | grep -q "\[installed\]")
then
   echo "[curl] -> [installed!]";
else
   echo "[curl] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'iputils-ping' | grep -q "\[installed\]")
then
   echo "[iputils-ping] -> [installed!]";
else
   echo "[iputils-ping] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


