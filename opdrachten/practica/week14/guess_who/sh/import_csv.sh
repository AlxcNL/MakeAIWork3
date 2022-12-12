#!/usr/bin/env bash

# https://www.mongodb.com/docs/database-tools/installation/installation/

mongoimport --db=PetHotel --type=csv --fields=_id,name,type --file=pets.csv
