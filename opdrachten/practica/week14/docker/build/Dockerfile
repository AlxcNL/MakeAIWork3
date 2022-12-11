# Default base image
ARG BASE_CONTAINER=$BASE_CONTAINER
ARG NB_USER=$NB_USER

# Use custom base image
FROM $BASE_CONTAINER

LABEL MAINTAINER="Jeroen Boogaard <j.a.boogaard@hr.nl>"

# Install python dependencies
COPY requirements.txt .
RUN python -m pip install --no-cache-dir -r requirements.txt

# Copy custom scripts
COPY run_script.sh /usr/local/bin/run_script

USER ${NB_USER}

RUN mkdir -p /home/student/notebooks \
    && mkdir -p /home/${NB_USER}/pics \
    && mkdir -p /home/student/projects \
    && mkdir -p /home/student/data

WORKDIR /home/${NB_USER}