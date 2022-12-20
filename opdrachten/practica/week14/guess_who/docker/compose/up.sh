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

mode=" -d"

# No composefile?
if [ $# -eq 0 ]
  then
    echo "No supplied"
    exit 1
fi

composeFile="$1"

cmd="${prefix}docker-compose -f ${composeFile} down && docker-compose -f ${composeFile} up${mode} --remove-orphans"
printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}