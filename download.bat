@echo off

rem
where python >nul 2>nul
if errorlevel 1 (
    echo Python not found
    pause
    exit
)

rem
echo Downloading...
python -m pip install -r requirements.txt
if errorlevel 1 (
    echo Error
    pause
    exit
)

echo Downloaded
pause