#!/bin/bash

# Resolve the project directory (parent of this script)
PROJECT_DIR=$(realpath "$(dirname "${BASH_SOURCE[0]}")")
VENV_PATH=$PROJECT_DIR"/venv"

#Create venv if it doesn't exist, and install requirements
if [[ ! -d $VENV_PATH ]]; then
    echo "Creating new virtual environment at $VENV_PATH"
    python3 -m venv $VENV_PATH
    echo "Installing dependencies from requirements.txt..."
    $VENV_PATH"/bin/python" -m pip install --upgrade pip
    $VENV_PATH"/bin/python" -m pip install -r $PROJECT_DIR/"requirements.txt"
fi

#Activate the virtual environment if not already active
if [[ $VIRTUAL_ENV != $VENV_PATH ]]; then
    echo "Activating virtual environment..."
    source $VENV_PATH/bin/activate
fi
