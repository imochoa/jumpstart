#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'gnome-themes-standard' | grep -q "\[installed\]")
then
   echo "[gnome-themes-standard] -> [installed!]";
else
   echo "[gnome-themes-standard] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'gtk2-engines-murrine' | grep -q "\[installed\]")
then
   echo "[gtk2-engines-murrine] -> [installed!]";
else
   echo "[gtk2-engines-murrine] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libglib2' | grep -q "\[installed\]")
then
   echo "[libglib2] -> [installed!]";
else
   echo "[libglib2] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


