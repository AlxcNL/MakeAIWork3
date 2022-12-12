#!/usr/bin/env bash

# https://hub.docker.com/_/neo4j/
docker run --rm -idt -p7474:7474 -p7687:7687 -v $PWD/data/neo4j:/data --env=NEO4J_AUTH=none neo4j:latest