#!/usr/bin/env sh
missing=0;


if $(apt list --installed 'i3' | grep -q "\[installed\]")
then
   echo "[i3] -> [installed!]";
else
   echo "[i3] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'arandr' | grep -q "\[installed\]")
then
   echo "[arandr] -> [installed!]";
else
   echo "[arandr] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'lxappearance' | grep -q "\[installed\]")
then
   echo "[lxappearance] -> [installed!]";
else
   echo "[lxappearance] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'dmenu' | grep -q "\[installed\]")
then
   echo "[dmenu] -> [installed!]";
else
   echo "[dmenu] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'rofi' | grep -q "\[installed\]")
then
   echo "[rofi] -> [installed!]";
else
   echo "[rofi] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'compton' | grep -q "\[installed\]")
then
   echo "[compton] -> [installed!]";
else
   echo "[compton] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3blocks' | grep -q "\[installed\]")
then
   echo "[i3blocks] -> [installed!]";
else
   echo "[i3blocks] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'xbacklight' | grep -q "\[installed\]")
then
   echo "[xbacklight] -> [installed!]";
else
   echo "[xbacklight] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'htop' | grep -q "\[installed\]")
then
   echo "[htop] -> [installed!]";
else
   echo "[htop] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'feh' | grep -q "\[installed\]")
then
   echo "[feh] -> [installed!]";
else
   echo "[feh] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3lock-fancy' | grep -q "\[installed\]")
then
   echo "[i3lock-fancy] -> [installed!]";
else
   echo "[i3lock-fancy] -> [NOT installed!]";
   missing=1;
fi


if $(apt list --installed 'i3-snapshot' | grep -q "\[installed\]")
then
   echo "[i3-snapshot] -> [installed!]";
else
   echo "[i3-snapshot] -> [NOT installed!]";
   missing=1;
fi


if [ "$missing" -eq "0" ];
then
    exit 0;
else
    exit 1;
fi


