#!/usr/bin/env bash

# Container

containerName="python-ai-mongo"

composePath="docker/compose"
composefile="${composePath}/python-ai-mongo.yaml"

cmd="docker/compose/up.sh ${composefile}"

printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}