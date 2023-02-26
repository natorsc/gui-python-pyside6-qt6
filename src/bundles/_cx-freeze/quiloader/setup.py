# -*- coding: utf-8 -*-
"""Python e Qt 6: Criando um bundle (pacote) com Cx_Freeze."""

import pathlib
import platform
import sys

from cx_Freeze import Executable, setup

from tools import make_translations

make_translations

BASE_DIR = pathlib.Path(__file__).resolve().parent
APP_ICON = str(BASE_DIR.joinpath(
    'resources', 'icons', 'br.com.justcode.Example.ico'),
)

base = None

build_exe_options = {
    'excludes': ['tkinter'],
    'include_files': ['forms', 'resources', 'sources', 'locales'],
}

if platform.system() == 'Windows':

    if sys.platform == 'win32':
        base = "Win32GUI"

    if sys.platform == 'win64':
        base = "Win64GUI"

setup(
    name='br.com.justcode.Example',
    author='Renato Cruz (natorsc@gmail.com)',
    version='0.0.1',
    description='Python e Qt 6: Criando um bundle (pacote) com Cx_Freeze.',
    options={'build_exe': build_exe_options},
    executables=[
        Executable(
            script='sources/MainWindow.py',
            target_name='br.com.justcode.Example',
            base=base,
            icon=APP_ICON,
        ),
    ],
)
