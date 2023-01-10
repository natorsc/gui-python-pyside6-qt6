# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QML ApplicationWindow{}."""

from pathlib import Path

from PySide6 import QtCore, QtGui, QtQml

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
SRC_DIR = BASE_DIR.parent.parent
QML_FILE = str(BASE_DIR.joinpath('MainWindow.qml'))
print(QML_FILE)
ICONS_DIR = SRC_DIR.joinpath('data', 'icons')
ICONS = {
    'window': str(ICONS_DIR.joinpath('br.com.justcode.Example.png')),
}


class MainWindow(QtCore.QObject):

    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    import sys

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

    application = QtGui.QGuiApplication(sys.argv)
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
