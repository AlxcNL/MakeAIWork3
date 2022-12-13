#!/usr/bin/env bash

argumentNames=("mode" "[script]")
argumentValues=("$@")
nrOfArguments=${#argumentValues[@]}

#  Image

name="jaboo/miw-notebook"
version="latest"
image="${name}:${version}"

if [ $nrOfArguments -lt 1 ]; then
    printf "USAGE: %s %s\n" "$0" "${argumentNames[*]}"
    exit 1;
fi

# Host

hostdirHome="${PWD}"
hostdirNotebooks="${hostdirHome}/notebooks"
hostdirData="${hostdirHome}/neo4j/data "

function makeWindowsProof {
    hostdirNotebooks=$(cygpath -w -p ${hostdirNotebooks})
    hostdirPics=$(cygpath -w -p ${hostdirPics})
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

export HOSTPATH_NOTEBOOKS=${hostdirNotebooks}
export HOSTPATH_DATA=${hostdirData}

# Container

mode="${argumentValues[0]}"

containerName="python-ai-${mode}"
containerHome="/home/student"
containerdirNotebooks="${containerHome}/notebooks"
containerdirData="${containerHome}/data"
composePath="docker/compose"
graphicsParams="-v \"/tmp/.X11-unix:/tmp/.X11-unix\" -e \"DISPLAY=${DISPLAY}\" --net=host"

cmd="${prefix}docker run -it --rm --name ${containerName}"
cmd="${cmd} -v \"${hostdirNotebooks}:${containerdirNotebooks}\""
cmd="${cmd} -v \"${hostdirPics}:${containerdirPics}\""
cmd="${cmd} -v \"${hostdirProjects}:${containerdirProjects}\""
cmd="${cmd} -v \"${hostdirData}:${containerdirData}\""
cmd="${cmd} ${graphicsParams}"

case "${mode}" in
    bash*)
        entryPoint="bash"
        cmd="${cmd} --entrypoint ${entryPoint} ${image}";;
    mongo*)
        version="latest"     
        composefile="${composePath}/python-ai-mongo.yaml"
        # export IMAGE=${image}
        export CONTAINER_NAME=${containerName}
        cmd="docker/compose/up.sh ${composefile}";;
    python-repl*)
        entryPoint="ptipython"
        cmd="${cmd} --entrypoint ${entryPoint} ${image}";;        
    python-script*)
        entryPoint="run_script"
        cmd="${cmd} -e SCRIPT=\"${argumentValues[1]}\" --entrypoint ${entryPoint} ${image}";;
    # Default
    *)      
        cmd="${cmd} ${image}";;        
esac

printf "%s cmd : \n\t%s\n\n" "$0" "${cmd}"
eval ${cmd}
