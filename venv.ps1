# Resolve the project directory (parent of this script)
$PROJECT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Definition

$VENV_PATH = Join-Path $PROJECT_DIR "venv"
$NEW_VENV = $false

# Check if virtual environment exists
if (-not (Test-Path $VENV_PATH)) {
    Write-Host "Creating new virtual environment at $VENV_PATH"
    python -m venv $VENV_PATH
    $NEW_VENV = $true
}

# Activate the virtual environment if not already active
if (-not $env:VIRTUAL_ENV -or $env:VIRTUAL_ENV -ne $VENV_PATH) {
    $activateScript = Join-Path $VENV_PATH "Scripts\Activate.ps1"
    Write-Host "Activating virtual environment..."
    & $activateScript
}

# Count installed packages (excluding header lines)
$PACKAGE_COUNT = (pip list | Measure-Object -Line).Lines - 2

if ($PACKAGE_COUNT -le 1 -or $NEW_VENV) {
    Write-Host "Installing dependencies from requirements.txt..."
    pip install -r (Join-Path $PROJECT_DIR "requirements.txt")
}
