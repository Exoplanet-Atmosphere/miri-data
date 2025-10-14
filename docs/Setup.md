## Virtual Enviornment Setup & Dependency Install

mac/linux: ```source venv.sh``` <br>
windows: ```. .\venv.ps1```

### If the venv setup script fails, here are some commands to troubleshoot

#### Manually create venv in root of project
mac/linux: ```python3 -m venv ./venv/``` <br>
windows: ```python -m venv .\venv```

#### Activate Venv
```source ./venv/bin/activate```

#### Install project dependencies using:
```pip install -r requirements.txt```

## Dependency Managment

#### install a new dependency:
mac/linux: ```python3 -m pip install (name of dependency)``` <br>
windows: ```python -m pip install (name of dependency)```

#### update dependencies list "requirements.txt" in project root using:
```pip freeze > requirements.txt```

## Run a Python3 Script
mac/linux: ```python3 (python filename)``` <br>
windows: ```python (python filename)```

## Deactivate Virtual Enviornment
```deactivate```