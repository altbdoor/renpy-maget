#!/usr/bin/bash

cd "$(dirname "$0")"
PROJECT_PATH=$(pwd)

if [[ "${SDK_PATH}" == "" ]]; then
    echo "Please specify SDK_PATH. Example:"
    echo "    SDK_PATH=/path/to/renpy-sdk bash build.sh"
    exit 1
fi

if [[ ! -f "${SDK_PATH}/renpy.sh" ]]; then
    echo "Unable to find Bash script for RenPy"
    echo "Maybe SDK_PATH is defined incorrectly?"
    exit 1
fi

cd "${SDK_PATH}"
bash renpy.sh ./ distribute "${PROJECT_PATH}" --package win --destination "${PROJECT_PATH}/dist" --no-update
