@echo off
REM Путь к вашей виртуальной среде
set VENV_PATH=C:\Calculations\env
REM Активируйте виртуальную среду
call %VENV_PATH%\Scripts\activate
REM Путь к вашему скрипту
set SCRIPT_PATH=C:\Calculations\FilterCalculationApp.py
REM Запуск скрипта
python %SCRIPT_PATH%
pause
