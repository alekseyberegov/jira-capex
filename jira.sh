#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
INI_FILE="jiracapex.ini"

user=$(awk -F "="  '/user/ {print $2}' ${SCRIPT_DIR}/${INI_FILE})
auth=$(awk -F "=" '/token/ {print $2}' ${SCRIPT_DIR}/${INI_FILE})

jql="project=OL"

curl -G \
  --user "${user}:${auth}" \
  --header 'Accept: application/json' \
  --data-urlencode "jql=${jql}" \
  "https://clicktripz.atlassian.net/rest/api/3/search" 
