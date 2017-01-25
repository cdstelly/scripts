#!/bin/bash
# cleanup all old containers..
docker ps -a | awk '{print $1}' | xargs docker rm
