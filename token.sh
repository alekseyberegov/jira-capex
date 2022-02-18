#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
INI_FILE="jiracapex.ini"

user=$(awk -F "="  '/user/ {print $2}' ${SCRIPT_DIR}/${INI_FILE})
auth=$(awk -F "=" '/token/ {print $2}' ${SCRIPT_DIR}/${INI_FILE})

echo -n ${user}:${auth} | base64

