@echo off
setlocal

cd /d "%~dp0"

python -m PyInstaller --onefile --windowed --icon=gfx\terranox.ico --name terranox game.py

xcopy gfx dist\gfx /E /I /Y
xcopy sfx dist\sfx /E /I /Y

echo Done!
pause
