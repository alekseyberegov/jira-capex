#!/bin/bash

array=(BAC PLAT DS CREATIVES ILV INF CU TWR ARCH ICO IEN IND PRD PROD)

for project in "${array[@]}"; do 
    echo "Loading ${project} ..."
    ./cli.sh load --map map_bac "project = ${project}  and created >= 2019-01-01" --max-results 1 --batch-size 1 --no-save
    sleep 2
done
