#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'exfat-fuse' | grep -q "\[installed\]")
then
   echo "[exfat-fuse] -> [installed!]";
else
   echo "[exfat-fuse] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'exfat-utils' | grep -q "\[installed\]")
then
   echo "[exfat-utils] -> [installed!]";
else
   echo "[exfat-utils] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


