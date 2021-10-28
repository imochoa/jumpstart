#!/usr/bin/env sh
# AUTOGENERATED FILE! DO NOT MODIFY

missing=0;

if $(apt list --installed 'arandr' | grep -q "\[installed\]")
then
   echo "[arandr] -> [installed!]";
else
   echo "[arandr] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'compton' | grep -q "\[installed\]")
then
   echo "[compton] -> [installed!]";
else
   echo "[compton] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'feh' | grep -q "\[installed\]")
then
   echo "[feh] -> [installed!]";
else
   echo "[feh] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'fonts-source-code-pro-ttf' | grep -q "\[installed\]")
then
   echo "[fonts-source-code-pro-ttf] -> [installed!]";
else
   echo "[fonts-source-code-pro-ttf] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'htop' | grep -q "\[installed\]")
then
   echo "[htop] -> [installed!]";
else
   echo "[htop] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3-gaps' | grep -q "\[installed\]")
then
   echo "[i3-gaps] -> [installed!]";
else
   echo "[i3-gaps] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3-gaps-wm' | grep -q "\[installed\]")
then
   echo "[i3-gaps-wm] -> [installed!]";
else
   echo "[i3-gaps-wm] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3-snapshot' | grep -q "\[installed\]")
then
   echo "[i3-snapshot] -> [installed!]";
else
   echo "[i3-snapshot] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3blocks' | grep -q "\[installed\]")
then
   echo "[i3blocks] -> [installed!]";
else
   echo "[i3blocks] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'lxappearance' | grep -q "\[installed\]")
then
   echo "[lxappearance] -> [installed!]";
else
   echo "[lxappearance] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'moka-icon-theme' | grep -q "\[installed\]")
then
   echo "[moka-icon-theme] -> [installed!]";
else
   echo "[moka-icon-theme] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'nordic' | grep -q "\[installed\]")
then
   echo "[nordic] -> [installed!]";
else
   echo "[nordic] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'rofi' | grep -q "\[installed\]")
then
   echo "[rofi] -> [installed!]";
else
   echo "[rofi] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'xbacklight' | grep -q "\[installed\]")
then
   echo "[xbacklight] -> [installed!]";
else
   echo "[xbacklight] -> [NOT installed!]";
   missing=1;
fi
