#!/bin/bash

docker pull mmcgarrigle/service_1

docker pull mmcgarrigle/service_2

docker pull mmcgarrigle/service_3

docker pull mmcgarrigle/service_4

docker rmi $(docker images -f "dangling=true" -q)