Dependency management currently using venv and requirements.txt

Virtual Enviornment Setup & Dependency Install

    To setup a new venv and install all project dependencies use shell scripts:
        mac/linux: source venv.sh
        windows: . .\venv.ps1


If the venv setup script fails, here are some commands to troubleshoot:

    in the root of the project create a virtual enviornment in a seperate folder:
        mac/linux: python3 -m venv ./venv/
        windows: python -m venv .\venv

    to enable the enviornment use:
        source ./venv/bin/activate

    get all project dependencies using:
        pip install -r requirements.txt

Dependency Managment

    install a new dependency:
        mac/linux: python3 -m pip install (name of dependency)
        windows: python -m pip install (name of dependency)

    update dependencies list "requirements.txt" in project root using:
        pip freeze > requirements.txt

Run a Python3 Script
    
    mac/linux: python3 (python filename)
    windows: python (python filename)

Deactivate Virtual Enviornment
    
    deactivate
