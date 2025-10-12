#!/bin/bash

PROJECT_DIR=$(realpath "${BASH_SOURCE[0]}"/..)

NEW_VENV=0 #false

if [[ ! -d $PROJECT_DIR/venv ]]; then
    echo $PROJECT_DIR/venv
    python3 -m venv $PROJECT_DIR/venv
    ((NEW_VENV=1))
fi

if [[ $VIRTUAL_ENV != $PROJECT_DIR/venv ]]; then
    source $PROJECT_DIR/venv/bin/activate
fi

PACKAGE_COUNT=$(pip list | wc -l)
((PACKAGE_COUNT-=2))

if [[ PACKAGE_COUNT -le 1 || NEW_VENV -eq 1 ]]; then
    pip install -r requirements.txt
fi
