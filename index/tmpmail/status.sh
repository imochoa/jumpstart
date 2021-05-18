#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'curl' | grep -q "\[installed\]")
then
   echo "[curl] -> [installed!]";
else
   echo "[curl] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'w3m' | grep -q "\[installed\]")
then
   echo "[w3m] -> [installed!]";
else
   echo "[w3m] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'jq' | grep -q "\[installed\]")
then
   echo "[jq] -> [installed!]";
else
   echo "[jq] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'sudo' | grep -q "\[installed\]")
then
   echo "[sudo] -> [installed!]";
else
   echo "[sudo] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'wget' | grep -q "\[installed\]")
then
   echo "[wget] -> [installed!]";
else
   echo "[wget] -> [NOT installed!]";
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


