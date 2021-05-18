#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'filemanager-actions' | grep -q "\[installed\]")
then
   echo "[filemanager-actions] -> [installed!]";
else
   echo "[filemanager-actions] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


