#!/usr/bin/bash

docker build .
docker tag cdstelly/scarf target:5000/scarf
docker push target:5000/scarf

docker pull target:5000/scarf
