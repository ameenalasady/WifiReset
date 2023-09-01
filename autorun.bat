@echo off
REM Open Windows Terminal as administrator and run the following commands
powershell -Command "Start-Process cmd -Verb RunAs -ArgumentList '/c start wt -d D:\GitHub\WifiReset -p \"Windows PowerShell\" python ./main.py'"
