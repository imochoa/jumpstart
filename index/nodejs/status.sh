#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'curl' | grep -q "\[installed\]")
then
   echo "[curl] -> [installed!]";
else
   echo "[curl] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'curl' | grep -q "\[installed\]")
then
   echo "[curl] -> [installed!]";
else
   echo "[curl] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed '-sL' | grep -q "\[installed\]")
then
   echo "[-sL] -> [installed!]";
else
   echo "[-sL] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'https' | grep -q "\[installed\]")
then
   echo "[https] -> [installed!]";
else
   echo "[https] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


