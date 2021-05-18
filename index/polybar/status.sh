#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'build-essential' | grep -q "\[installed\]")
then
   echo "[build-essential] -> [installed!]";
else
   echo "[build-essential] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'git' | grep -q "\[installed\]")
then
   echo "[git] -> [installed!]";
else
   echo "[git] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'cmake' | grep -q "\[installed\]")
then
   echo "[cmake] -> [installed!]";
else
   echo "[cmake] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'cmake-data' | grep -q "\[installed\]")
then
   echo "[cmake-data] -> [installed!]";
else
   echo "[cmake-data] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'pkg-config' | grep -q "\[installed\]")
then
   echo "[pkg-config] -> [installed!]";
else
   echo "[pkg-config] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-sphinx' | grep -q "\[installed\]")
then
   echo "[python3-sphinx] -> [installed!]";
else
   echo "[python3-sphinx] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libcairo2-dev' | grep -q "\[installed\]")
then
   echo "[libcairo2-dev] -> [installed!]";
else
   echo "[libcairo2-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb1-dev' | grep -q "\[installed\]")
then
   echo "[libxcb1-dev] -> [installed!]";
else
   echo "[libxcb1-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb-util0-dev' | grep -q "\[installed\]")
then
   echo "[libxcb-util0-dev] -> [installed!]";
else
   echo "[libxcb-util0-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb-randr0-dev' | grep -q "\[installed\]")
then
   echo "[libxcb-randr0-dev] -> [installed!]";
else
   echo "[libxcb-randr0-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb-composite0-dev' | grep -q "\[installed\]")
then
   echo "[libxcb-composite0-dev] -> [installed!]";
else
   echo "[libxcb-composite0-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'python3-xcbgen' | grep -q "\[installed\]")
then
   echo "[python3-xcbgen] -> [installed!]";
else
   echo "[python3-xcbgen] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'xcb-proto' | grep -q "\[installed\]")
then
   echo "[xcb-proto] -> [installed!]";
else
   echo "[xcb-proto] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb-image0-dev' | grep -q "\[installed\]")
then
   echo "[libxcb-image0-dev] -> [installed!]";
else
   echo "[libxcb-image0-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb-ewmh-dev' | grep -q "\[installed\]")
then
   echo "[libxcb-ewmh-dev] -> [installed!]";
else
   echo "[libxcb-ewmh-dev] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'libxcb-icccm4-dev' | grep -q "\[installed\]")
then
   echo "[libxcb-icccm4-dev] -> [installed!]";
else
   echo "[libxcb-icccm4-dev] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


