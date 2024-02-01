@echo off

python -c "import sys" >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or is not available in PATH. Install the newest python from here: https://www.python.org/downloads/
)

pause
