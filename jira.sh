#!/bin/bash

if [ "$1" == "" ] 
then
  echo "Usage: $0 <jql>"
  exit 1
fi

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
INI_FILE="jiracapex.ini"

user=$(awk -F "="  '/user/ {print $2}' ${SCRIPT_DIR}/${INI_FILE})
auth=$(awk -F "=" '/token/ {print $2}' ${SCRIPT_DIR}/${INI_FILE})

jql="$1"

curl -G \
  --user "${user}:${auth}" \
  --header 'Accept: application/json' \
  --data-urlencode "jql=${jql}" \
  "https://clicktripz.atlassian.net/rest/api/3/search" 
