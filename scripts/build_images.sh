#!/bin/bash

# Print image list before build

echo $(docker images)

#Build service_1 image

docker build --no-cache -t mmcgarrigle/service_1 ./Service_1
docker push mmcgarrigle/service_1:latest

# Build service_2 image

docker build --no-cache -t mmcgarrigle/service_2 ./Service_2
docker push mmcgarrigle/Service_2:latest

# Build service_3 image

docker build --no-cache -t mmcgarrigle/service_3 ./Service_3
docker push mmcgarrigle/service_3:latest

# Build service_4 image

docker build --no-cache -t mmcgarrigle/service_4 ./Service_4
docker push mmcgarrigle/service_4:latest