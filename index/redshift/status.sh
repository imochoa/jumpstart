#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'redshift' | grep -q "\[installed\]")
then
   echo "[redshift] -> [installed!]";
else
   echo "[redshift] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'redshift-gtk' | grep -q "\[installed\]")
then
   echo "[redshift-gtk] -> [installed!]";
else
   echo "[redshift-gtk] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


