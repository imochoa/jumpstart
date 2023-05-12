#!/bin/bash

docker run --rm -v "$PWD:/mnt" koalaman/shellcheck:stable myscript
# Or :v0.4.7 for that version, or :latest for daily builds
