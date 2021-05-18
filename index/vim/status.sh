#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'vim' | grep -q "\[installed\]")
then
   echo "[vim] -> [installed!]";
else
   echo "[vim] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'vim-gtk' | grep -q "\[installed\]")
then
   echo "[vim-gtk] -> [installed!]";
else
   echo "[vim-gtk] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


