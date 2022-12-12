#!/usr/bin/env bash

# Host

hostdirHome="${PWD}"
hostdirData="${hostdirHome}/db"

function makeWindowsProof {
    hostdirData=$(cygpath -w -p ${hostdirData})
    prefix="winpty "
}

# Windows environment?
prefix=""
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     machine="Linux";;
    Darwin*)    machine="Mac";;
    CYGWIN*)    machine="Cygwin" && makeWindowsProof;;
    MINGW*)     machine="Git Bash" && makeWindowsProof;;
    *)          machine="UNKNOWN:${os}"
esac

# Container

mode="${argumentValues[0]}"

containerName="python-ai-${mode}"
containerHome="/home/student"
containerdirData="${containerHome}/db"
composePath="docker/compose"
composefile="${composePath}/python-ai-mongo.yaml"

export HOSTPATH_DATA=${hostdirData}
export CONTAINER_NAME=${containerName}
export CONTAINER_DATA=${containerdirData}

export HOSTPATH_DATA=${hostdirData}
cmd="${prefix}docker/compose/up.sh ${composefile}"

printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}
