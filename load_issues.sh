#!/bin/bash

if [[ "$1" == "" ]] ; then
    echo "Usage: $0 YYYY-MM-DD"
    exit 1
fi

SCRIPT_DIR="$( cd -- "$( dirname -- "${BASH_SOURCE[0]:-$0}"; )" &> /dev/null && pwd 2> /dev/null; )";

echo ${SCRIPT_DIR}
start_at="$1"

maps=(map_arch map_bac map_creatives map_cu map_ds map_ico map_ien map_ilv map_ind map_inf map_plat map_prd map_prod map_tower map_twr)

set -o xtrace

echo "" > ~/load_issues.log

for m in "${maps[@]}"
do
    project=${m#*_}
    project=$(echo "${project}" | tr '[:lower:]' '[:upper:]')
    ${SCRIPT_DIR}/cli.sh load --map "${m}"  "project = ${project} and created >= ${start_at}" --max-results 100000
    echo "DONE: ${m} ${project} ${start_at}" >> ~/load_issues.log
done
