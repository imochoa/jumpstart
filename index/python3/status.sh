#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'python3' | grep -q "\[installed\]")
then
   echo "[python3] -> [installed!]";
else
   echo "[python3] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-pip' | grep -q "\[installed\]")
then
   echo "[python3-pip] -> [installed!]";
else
   echo "[python3-pip] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-venv' | grep -q "\[installed\]")
then
   echo "[python3-venv] -> [installed!]";
else
   echo "[python3-venv] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-dev' | grep -q "\[installed\]")
then
   echo "[python3-dev] -> [installed!]";
else
   echo "[python3-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'build-essential' | grep -q "\[installed\]")
then
   echo "[build-essential] -> [installed!]";
else
   echo "[build-essential] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libssl-dev' | grep -q "\[installed\]")
then
   echo "[libssl-dev] -> [installed!]";
else
   echo "[libssl-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libffi-dev' | grep -q "\[installed\]")
then
   echo "[libffi-dev] -> [installed!]";
else
   echo "[libffi-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxml2-dev' | grep -q "\[installed\]")
then
   echo "[libxml2-dev] -> [installed!]";
else
   echo "[libxml2-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxslt1-dev' | grep -q "\[installed\]")
then
   echo "[libxslt1-dev] -> [installed!]";
else
   echo "[libxslt1-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'zlib1g-dev' | grep -q "\[installed\]")
then
   echo "[zlib1g-dev] -> [installed!]";
else
   echo "[zlib1g-dev] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


