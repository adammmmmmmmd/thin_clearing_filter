@echo off
REM Путь к вашей виртуальной среде
set VENV_PATH=C:\Calculations\env
REM 
call %VENV_PATH%\Scripts\activate
REM 
set SCRIPT_PATH=C:\Calculations\TONFILD.py
REM 
python %SCRIPT_PATH%
pause
