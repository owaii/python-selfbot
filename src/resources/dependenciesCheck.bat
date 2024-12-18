@echo off

python -c "import sys" >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed or is not available in PATH. Install the newest Python from here: https://www.python.org/downloads/
    pause
    exit /b 1
)

python -c "import requests" >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is installed, but the 'requests' library is not. Install it by running: pip install requests
    pause
    exit /b 1
)

python -c "import tqdm" >nul 2>&1
if %errorlevel% neq 0 (
    echo The 'tqdm' library is not installed. Install it by running: pip install tqdm
    pause
    exit /b 1
)

python -c "import selenium" >nul 2>&1
if %errorlevel% neq 0 (
    echo The 'selenium' library is not installed. Install it by running: pip install selenium
    pause
    exit /b 1
)

python -c "import pyperclip" >nul 2>&1
if %errorlevel% neq 0 (
    echo The 'pyperclip' library is not installed. Install it by running: pip install pyperclip
    pause
    exit /b 1
)

python -c "import webdriver_manager" >nul 2>&1
if %errorlevel% neq 0 (
    echo The 'webdriver_manager' library is not installed. Install it by running: pip install webdriver-manager
    pause
    exit /b 1
)

echo Python is installed, and all required libraries are available.
pause
