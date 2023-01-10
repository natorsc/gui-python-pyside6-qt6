# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QML style.

Estilos disponíveis: 'Basic', Fusion, 'Imagine', 'Material' e 'Universal'.

https://doc-snapshots.qt.io/qtforpython-6.2/overviews/qtquickcontrols2-styles.html
"""

from pathlib import Path

from PySide6 import QtCore, QtGui, QtQml

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
QML_FILE = str(BASE_DIR.joinpath('MainWindow.qml'))
ICONS_DIR = SRC_DIR.joinpath('data', 'icons')
ICONS = {
    'window': str(ICONS_DIR.joinpath('br.com.justcode.Example.png')),
}


class MainWindow(QtCore.QObject):

    def __init__(self):
        super().__init__()

    @QtCore.Slot(str, result=str)
    def on_button_clicked(self, text):
        if text.split():
            return text
        else:
            return 'Digite algo no campo de texto ;).'


if __name__ == '__main__':
    import os
    import sys

    # Escolha apenas uma forma de definir o estilo.
    from PySide6.QtQuickControls2 import QQuickStyle

    # Adicionando o estilo via arquivo de configuração.
    # (qtquickcontrols2.conf + resources.qrc).
    # `pyside6-rcc resources.qrc -o resources_rc.py`.
    import resources_rc

    # Atribuindo para o PyCharm não remover.
    RESOURCES_RC = resources_rc

    # Adicionando o estilo via QQuickStyle:
    QQuickStyle.setStyle('Material')

    # Adicionando o estilo via variável de ambiente:
    os.environ['QT_QUICK_CONTROLS_STYLE'] = 'Material'
    os.environ['QT_QUICK_CONTROLS_MATERIAL_THEME'] = 'Light'
    os.environ['QT_QUICK_CONTROLS_MATERIAL_ACCENT'] = 'Teal'
    os.environ['QT_QUICK_CONTROLS_MATERIAL_PRIMARY'] = 'BlueGrey'

    APPLICATION_NAME = 'br.com.justcode.Example'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    current_platform = sys.platform
    if current_platform == 'win32' or current_platform == 'win64':
        from ctypes import windll

        windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APPLICATION_NAME,
        )
    elif current_platform == 'linux':
        from os import environ, getenv

        XDG_SESSION_TYPE = getenv('XDG_SESSION_TYPE')
        if XDG_SESSION_TYPE == 'wayland':
            environ['QT_QPA_PLATFORM'] = 'wayland'
        elif XDG_SESSION_TYPE is None:
            environ['QT_QPA_PLATFORM'] = 'xcb'

    # Adicionando o estilo via comando:
    application = QtGui.QGuiApplication(sys.argv + ['-style', 'Material'])
    application.setWindowIcon(QtGui.QIcon(ICONS['window']))
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(f'{APPLICATION_NAME}.desktop')

    mainwindow = MainWindow()

    engine = QtQml.QQmlApplicationEngine()
    engine.rootContext().setContextProperty('mainwindow', mainwindow)
    engine.load(QtCore.QUrl.fromLocalFile(QML_FILE))
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(application.exec())
