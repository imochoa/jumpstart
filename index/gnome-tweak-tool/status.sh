#!/usr/bin/env sh

# DO NOT MODIFY!
# THIS FILE WAS AUTOGENERATED BY *generate-status-files.py*

missing=0;


if $(apt list --installed 'gnome-tweak-tool' | grep -q "\[installed\]")
then
   echo "[gnome-tweak-tool] -> [installed!]";
else
   echo "[gnome-tweak-tool] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'gnome-tweaks' | grep -q "\[installed\]")
then
   echo "[gnome-tweaks] -> [installed!]";
else
   echo "[gnome-tweaks] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi

