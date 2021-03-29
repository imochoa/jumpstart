#!/usr/bin/env bash
sudo rm -f /usr/local/bin/gprof2dot.py
sudo wget https://raw.githubusercontent.com/jrfonseca/gprof2dot/master/gprof2dot.py --continue --output-document=/usr/local/bin/gprof2dot.py
sudo chmod +x /usr/local/bin/gprof2dot.py
# Usage:
# python -m cProfile -o foo.stats foo.py
$ gprof2dot foo.stats -f pstats > foo.dot
