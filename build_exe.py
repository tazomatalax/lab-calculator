"""
Build script to create an executable using PyInstaller
"""
import PyInstaller.__main__
import os
import sys
import shutil

# Clean previous build directories
if os.path.exists("./dist"):
    shutil.rmtree("./dist")
if os.path.exists("./build"):
    shutil.rmtree("./build")

# Define PyInstaller command arguments
args = [
    'main.py',                              # Script to build
    '--name=LabCalculator',                 # Name of the executable
    '--onefile',                            # Create a single executable
    '--windowed',                           # Windows application (no console)
    '--icon=NONE',                          # No icon for now, can add one later
    '--add-data=calc_modules;calc_modules', # Include the calculation modules
    '--clean',                              # Clean PyInstaller cache
]

# For PyQt5, we need to explicitly include all plugins to ensure the app works correctly
hidden_imports = [
    '--hidden-import=PyQt5',
    '--hidden-import=PyQt5.QtCore',
    '--hidden-import=PyQt5.QtGui',
    '--hidden-import=PyQt5.QtWidgets'
]

args.extend(hidden_imports)

# Add platform-specific arguments
if sys.platform.startswith('win'):
    # For Windows
    args.append('--noconsole')  # No console window in Windows

# Run PyInstaller
PyInstaller.__main__.run(args)