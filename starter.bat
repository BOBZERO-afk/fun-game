@echo off
cd /d "%~dp0"
setlocal

set PYTHON_EXE=python

:CheckAdmin
net session >nul 2>&1
if %errorlevel% neq 0 (
    powershell -Command "Start-Process '%PYTHON_EXE%' -ArgumentList '%~1' -Verb RunAs"
    exit /b
)
goto :eof

if not exist needs.txt (
    echo re>needs.txt
    echo urllib>>needs.txt
    echo ctypes>>needs.txt
    echo packaging>>needs.txt
    echo XNOR_module>>needs.txt
    echo tkinter>>needs.txt
)


title Downloading modules...
echo This may take some time, please do not exit this program

call :CheckAdmin "download_modules.py"

"%PYTHON_EXE%" "download_modules.py"
timeout /t 3 /nobreak >nul

title Checking Python version...

call :CheckAdmin "check python ver.py"

"%PYTHON_EXE%" "check python ver.py"
timeout /t 20 /nobreak >nul

title Start of main file...
echo Starting main file...

call :CheckAdmin "main.py"

"%PYTHON_EXE%" "main.py"

timeout /t 3 /nobreak >nul
cls

echo Thank you for using this program
pause
exit /b 0