#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'virtualbox' | grep -q "\[installed\]")
then
   echo "[virtualbox] -> [installed!]";
else
   echo "[virtualbox] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'virtualbox-dkms' | grep -q "\[installed\]")
then
   echo "[virtualbox-dkms] -> [installed!]";
else
   echo "[virtualbox-dkms] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'virtualbox-ext-pack' | grep -q "\[installed\]")
then
   echo "[virtualbox-ext-pack] -> [installed!]";
else
   echo "[virtualbox-ext-pack] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'virtualbox-guest-dkms' | grep -q "\[installed\]")
then
   echo "[virtualbox-guest-dkms] -> [installed!]";
else
   echo "[virtualbox-guest-dkms] -> [NOT installed!]";
   missing=1;
fi