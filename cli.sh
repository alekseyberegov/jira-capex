#!/bin/bash

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
export PYTHONPATH="${SCRIPT_DIR}:${PYTHONPATH}"

python ${SCRIPT_DIR}/jiracapex/cli/cli.py --home "${SCRIPT_DIR}" "${@:1}"
status=$?

exit $status
