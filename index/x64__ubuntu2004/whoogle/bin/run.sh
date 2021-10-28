#!/usr/bin/env bash

container_name='whoogle-search'
port='5000'
url="http://localhost:${port}/"
img="benbusby/whoogle-search"

# mount config!
# https://github.com/benbusby/whoogle-search/issues/31

# https://hub.docker.com/layers/benbusby/whoogle-search/config-volume/images/sha256-6dfddcd180219a87fc601714401bbc60477db4be2249307667f1935af3988c06?context=explore

if [ ! "$(docker ps -q -f name=${container_name})" ]; then
    if [ "$(docker ps -aq -f status=exited -f name=${container_name})" ]; then
        # cleanup
        docker rm ${container_name}
    fi
    # run your container
    echo "Looking for updates...";

    docker pull ${img};

    # 'dark'
    # 'system'

      # --env WHOOGLE_CONFIG_THEME='system'       \
      #  --env  WHOOGLE_CONFIG_LANGUAGE='English'        \
      #   --env WHOOGLE_CONFIG_SEARCH_LANGUAGE='English' \
      #   --env WHOOGLE_CONFIG_NEW_TAB=1 \

    docker run                              \
      --detach                              \
      --rm                                  \
      -v whoogle_config:/config             \
      -p ${port}:5000                       \
      --name=${container_name}              \
      ${img}:latest                         \
      && echo "Starting whoogle at ${url}...";
else
    echo "Already running!";
    echo "Check: ${url}";
fi
