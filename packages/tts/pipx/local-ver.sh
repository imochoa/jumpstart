#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: local-ver.sh
#		 >     Name: TTS
#		 > Template: pipx

pipx list | grep installed | grep TTS | ts -s ' ' | cut -d' ' -f8
