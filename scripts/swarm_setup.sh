#!/bin/bash

if [[ "$(docker node ls 2> /dev/null)" == "" ]]; then
    docker swarm init
else
    docker node ls
fi