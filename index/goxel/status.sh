#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'scons' | grep -q "\[installed\]")
then
   echo "[scons] -> [installed!]";
else
   echo "[scons] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'pkg-config' | grep -q "\[installed\]")
then
   echo "[pkg-config] -> [installed!]";
else
   echo "[pkg-config] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libglfw3-dev' | grep -q "\[installed\]")
then
   echo "[libglfw3-dev] -> [installed!]";
else
   echo "[libglfw3-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libgtk-3-dev' | grep -q "\[installed\]")
then
   echo "[libgtk-3-dev] -> [installed!]";
else
   echo "[libgtk-3-dev] -> [NOT installed!]";
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


