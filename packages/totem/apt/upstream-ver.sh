#!/bin/bash

# <<<AUTOGENERATED - DO NOT MODIFY>>>
#		 >     File: upstream-ver.sh
#		 >     Name: totem
#		 > Template: apt

printf "gstreamer1.0-libav > %s\n" "$(apt-cache policy gstreamer1.0-libav | grep Candidate | cut -d: -f2 | tr -d /" /")"
