#!/usr/bin/env sh

# DO NOT MODIFY!
# THIS FILE WAS AUTOGENERATED BY *generate-status-files.py*

missing=0;


if $(apt list --installed 'openvpn' | grep -q "\[installed\]")
then
   echo "[openvpn] -> [installed!]";
else
   echo "[openvpn] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'easy-rsa' | grep -q "\[installed\]")
then
   echo "[easy-rsa] -> [installed!]";
else
   echo "[easy-rsa] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'network-manager-openvpn' | grep -q "\[installed\]")
then
   echo "[network-manager-openvpn] -> [installed!]";
else
   echo "[network-manager-openvpn] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


