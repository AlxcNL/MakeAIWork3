#!/usr/bin/env bash

virtualEnvName="miw3"

function createVirtualEnv {    
    if [[ -d "" ]]
    then
        printf "Virtual environment %s already exists" ${virtualEnvName}
    else
        printf "Create virtual environment %s" ${virtualEnvName}
        python -m pip install virtualenv
        python -m venv ${virtualEnvName} 
    fi	

    printf "Activate virtual environment %s\n" ${virtualEnvName}
    source ${virtualEnvName}/Scripts/activate

    # Make sure ~/.bashrc exists
    touch ~/.bashrc 
    (cat ~/.bashrc | grep ${virtualEnvName}) && exit 1
    echo "Add virtual environment activation to bashrc"
    activationPath=$(cygpath ${PWD}/${virtualEnvName}/Scripts/activate)
    echo "${activationPath}"
    echo "source ${activationPath}" >> ~/.bashrc    

    echo "Create alias pptyhon for ptpython which starts with winpty"
    alias ppython="winpty ptpython"

}

function createCondaEnv {
    if (! command -v "zsh" &> /dev/null ) then
        error "You need to install zsh first!" && exit 0
    else
        if (! command -v "conda" &> /dev/null ) then
            error "You need to install Miniconda first!" && exit 0
        else
            echo "Add virtual environment activation to zshrc"
            ( cat ~/.conda/environments.txt | grep ${virtualEnvName} ) || ( printf "Create virtual environment %s\n" ${virtualEnvName} && conda create -n ${virtualEnvName} )
            ( cat ~/.zshrc | grep ${virtualEnvName} ) || printf "conda activate %s\n" ${virtualEnvName} >> ~/.zshrc
            echo "Restart your terminal and run install/install_requirements.sh" 
        fi

    fi

}

echo "Detect OS"
unameOut="$(uname -s)"
os="${unameOut:0:7}"

case "${os}" in
    Linux*)     
        createCondaEnv
    ;;
    # MacOS
    Darwin*)
        createCondaEnv
    ;;
    # Git Bash
    MINGW*)     
        createVirtualEnv
    ;;
    *)          
        createVirtualEnv
    ;;

esac
