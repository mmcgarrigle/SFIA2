#!/bin/bash

docker service update --image mmcgarrigle/service_1:latest Riddleservice_service_1
docker service update --image mmcgarrigle/service_2:latest Riddleservice_service_2
docker service update --image mmcgarrigle/service_3:latest Riddleservice_service_3
docker service update --image mmcgarrigle/service_4:latest Riddleservice_service_4
# docker rmi $(docker images -f "dangling=true" -q) -f

docker system prune -f