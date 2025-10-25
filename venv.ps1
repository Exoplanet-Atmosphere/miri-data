#Resolve the project directory (parent of this script)
$PROJECT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition
$VENV_PATH = Join-Path $PROJECT_DIR "venv"

#Create venv if it doesn't exist, and install requirements
if (-not (Test-Path $VENV_PATH)) {
    Write-Host "Creating new virtual environment at $VENV_PATH"
    python -m venv $VENV_PATH
    Write-Host "Installing dependencies from requirements.txt..."
    & (Join-Path $VENV_PATH "Scripts\python.exe") -m pip install --upgrade pip
    & (Join-Path $VENV_PATH "Scripts\python.exe") -m pip install -r (Join-Path $PROJECT_DIR "requirements.txt")
}

#Activate the virtual environment if not already active
if (-not $env:VIRTUAL_ENV -or $env:VIRTUAL_ENV -ne $VENV_PATH) {
    $activateScript = Join-Path $VENV_PATH "Scripts\Activate.ps1"
    Write-Host "Activating virtual environment..."
    . $activateScript  #dot source to persist in shell
}

#install missing depencies if applicable
$MISSING_DEPS = & (Join-Path $VENV_PATH Scripts\python.exe) -m pip install --dry-run | Select-String -Pattern "Would install"

if ($MISSING_DEPS) {
    Write-Host "Updating Dependencies..."
    & (Join-Path $VENV_PATH "Scripts\python.exe") -m pip install --upgrade pip
    & (Join-Path $VENV_PATH "Scripts\python.exe") -m pip install -r (Join-Path $PROJECT_DIR "requirements.txt")
}