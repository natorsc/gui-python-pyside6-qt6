# -*- coding: utf-8 -*-
"""Python e Qt 6: Criando um bundle (pacote) com Cx_Freeze."""

import pathlib
import subprocess

LANGS = ['pt_BR']

BASE_DIR = pathlib.Path(__file__).resolve().parent
ROOT_DIR = BASE_DIR.parent
FORMS_DIR = ROOT_DIR.joinpath('forms')

for lang in LANGS:
    ts_dir = ROOT_DIR.joinpath('translations', lang)
    ts_dir.mkdir(parents=True, exist_ok=True)

    qm_dir = ROOT_DIR.joinpath('locales', lang)
    qm_dir.mkdir(parents=True, exist_ok=True)

    for ui_file in FORMS_DIR.rglob('*.ui'):
        ts_output = ts_dir.joinpath(ui_file.stem)

        subprocess.call(
            args=['pyside6-lupdate', f'{ui_file}',
                  '-ts', f'{ts_output}.ts'],
            cwd=ROOT_DIR,
        )

        subprocess.call(
            args=['pyside6-lrelease', f'{ts_output}.ts',
                  '-qm', f'{qm_dir.joinpath(ui_file.stem)}.qm'],
            cwd=ROOT_DIR,
        )
