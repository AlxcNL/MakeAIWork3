#!/usr/bin/env bash

  if (! command -v "conda" &> /dev/null ) then
    echo "Install with pip\n"
    python -m pip install --upgrade pip
    python -m pip install --no-cache-dir -r requirements.txt

  else
    conda update -n base -c conda-forge conda
    conda install --yes -c conda-forge \
      neo4j \
      neo4j-driver \
      opencv \
      pathlib \
      pymongo \
      py2neo \
      pyspark \
      scrapy

  fi