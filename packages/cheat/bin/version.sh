#!/usr/bin/env sh

VER=$(git ls-remote --refs --tags https://github.com/cheat/cheat |
      cut --delimiter='/' --fields=3 |
      tail --lines=1)

echo "cheat -> [${VER}]"
