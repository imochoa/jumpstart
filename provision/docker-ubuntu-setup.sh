#!/usr/bin/env bash
export DEBIAN_FRONTEND=noninteractive \
&& apt-get update \
&& apt-get install -y --no-install-recommends \
                    tzdata \
                    keyboard-configuration \
&& apt-get -y install sudo

# https://stackoverflow.com/questions/46247032/how-to-solve-invoke-rc-d-policy-rc-d-denied-execution-of-start-when-building
printf '#!/bin/sh\nexit 0' > /usr/sbin/policy-rc.d

# For (invoke-rc.d: could not determine current runlevel)
export RUNLEVEL=1
