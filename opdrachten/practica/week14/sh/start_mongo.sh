#!/usr/bin/env bash

runnable="docker"
containerName="python-ai-mongo"
cmd="docker/run/miw_container.sh mongo"
printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}