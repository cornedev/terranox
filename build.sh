#!/bin/bash
set -e
cd "$(dirname "$0")"
python -m PyInstaller --onefile --windowed --icon=gfx/terranox.ico --name terranox game.py
cp -r gfx dist/gfx
cp -r sfx dist/sfx
