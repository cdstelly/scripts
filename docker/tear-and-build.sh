#!/bin/bash
docker service rm es-swarm_gateway
docker service rm es-swarm_data
docker service rm es-swarm_master

docker service rm esswarm_opennsfw
docker service rm esswarm_data
docker service rm esswarm_bulkextractor
docker service rm esswarm_exif

docker service rm scarf_consumer

## startup
cd esswarm && docker deploy esswarm

## broker will need to be up for these containers to be viable, ok to start them up first and just let them fail
docker service create --name esswarm_bulkextractor --network esswarm_scarfelastic trex0:5000/esswarm_bulkextractor
docker service create --name esswarm_exif          --network esswarm_scarfelastic trex0:5000/esswarm_exif
docker service create --name esswarm_opennsfw      --network esswarm_scarfelastic trex0:5000/esswarm_opennsfw
docker service scale esswarm_master=2
docker service scale esswarm_bulkextractor=2
docker service scale esswarm_exif=2
docker service scale esswarm_opennsfw=2

docker service create --name scarf_consumer --network esswarm_scarfelastic trex0:5000/scarf_consumer
























Docker sucks.
