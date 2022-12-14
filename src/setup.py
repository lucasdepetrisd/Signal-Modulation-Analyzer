import sys
import os
from cx_Freeze import setup, Executable

import scipy
includefiles_list=[]
scipy_path = os.path.dirname(scipy.__file__)

# ADD FILES
files = ['cil-fsk.ico']
files.append(scipy_path)

# TARGET
target = Executable(
    script="main.py",
    base="Win32GUI",
    icon="cil-fsk.ico"
)

# SETUP CX FREEZE
setup(
    name = "SigMA",
    version = "0.8",
    description = "Simulador de Modulaciones en Señales",
    author = "Lucas Depetris",
    options = {'build_exe' : {'include_files': files}},
    executables = [target]
)