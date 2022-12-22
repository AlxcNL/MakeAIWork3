#!/usr/bin/env bash

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

containerName="python-ai-neo"
composePath="docker/compose"
composefile="${composePath}/python-ai-neo.yaml"

cmd="${prefix}docker/compose/up.sh ${composefile}"

printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}