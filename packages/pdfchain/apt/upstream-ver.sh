#!/usr/bin/env sh

# <<<AUTOGENERATED FILE - DO NOT MODIFY>>>

printf "pdfchain > %s\n" "$(apt-cache policy pdfchain | grep Candidate | cut -d: -f2 | tr -d /" /")"
