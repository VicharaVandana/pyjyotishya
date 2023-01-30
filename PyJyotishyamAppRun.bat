@echo off
rem change to current directory
cd /D "%~dp0"

echo %cd%
echo "You need python 3 and some special libraries to run this app."
echo "If it doesnt run properly then see the error displayed and fix them. Mostly you need to install needed python modules."
echo "to install a python module just run the command shown below"
echo "pip install <module name>"

python jyotishyamgui.py
pause