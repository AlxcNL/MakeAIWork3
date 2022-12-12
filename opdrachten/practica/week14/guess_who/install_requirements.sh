#!/usr/bin/env bash

  if (! command -v "conda" &> /dev/null ) then
    echo "Install with pip\n"
    python -m pip install --upgrade pip
    python -m pip install --no-cache-dir -r requirements.txt

  else
    conda update -n base -c conda-forge conda
    conda install --yes -c conda-forge \
      opencv \
      pathlib \
      pymongo \
      pydata \
      pyspark \
      scrapy

  fi


