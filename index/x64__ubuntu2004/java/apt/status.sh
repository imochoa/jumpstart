#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'default-jre' | grep -q "\[installed\]")
then
   echo "[default-jre] -> [installed!]";
else
   echo "[default-jre] -> [NOT installed!]";
   missing=1;
fi