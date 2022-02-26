#!/bin/bash

array=(BAC PLAT DS CREATIVES ILV INF CU TWR ARCH ICO IEN IND PRD PROD)

for project in "${array[@]}"; do 
    map_siffix=$(echo "${project}" | tr '[:upper:]' '[:lower:]')
    echo "Loading ${project} / ${map_siffix} ..."
    ./cli.sh load --map map_${map_siffix} "project = ${project} and created >= 2019-01-01" --max-results 100000 --batch-size 100
    sleep 2
done
