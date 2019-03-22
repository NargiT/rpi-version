#!/usr/bin/env bash
if [ $TRAVIS_PULL_REQUEST == "false" ]; then
    docker login -u="$DOCKER_USER" -p="$DOCKER_PASS"
    TAG=$(grep "ENV RPI_VERSION" Dockerfile | awk 'NF>1{print $NF}')
    docker tag "nargit/rpi-version nargit/rpi-version:$TAG"
    docker push "nargit/rpi-version:$TAG"
    docker push nargit/rpi-version
fi
