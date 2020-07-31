#!/bin/bash

docker build --no-cache -t mmcgarrigle/service_1 ./Service_1
docker push mmcgarrigle/service_1:latest

docker build --no-cache -t mmcgarrigle/service_2 ./Service_2
docker push mmcgarrigle/service_2:latest

docker build --no-cache -t mmcgarrigle/service_3 ./Service_3
docker push mmcgarrigle/service_3:latest

docker build --no-cache -t mmcgarrigle/service_4 ./Service_4
docker push mmcgarrigle/service_4:latest