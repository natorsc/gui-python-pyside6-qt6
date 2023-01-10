# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QTimer() com QUiLoader()."""

from pathlib import Path

from PySide6 import QtCore, QtUiTools, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
UI_FILE = str(BASE_DIR.joinpath('MainWindow.ui'))


class MainWindow(QtCore.QObject):
    counter = 0

    def __init__(self, application):
        super().__init__()
        self.application = application

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(UI_FILE)

        self.ui.action_exit.triggered.connect(self.on_action_exit_clicked)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.start_timer)
        # Intervalo de tempo que o método será chamado.
        self.timer.start(1000)

    def on_action_exit_clicked(self):
        self.application.quit()

    def show_window(self):
        self.ui.show()

    def start_timer(self):
        print(f'{self.counter} - O método foi executado.')
        self.counter += 1
        if self.counter == 6:
            self.timer.stop()
            print('Timer foi parado.')


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

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

        QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

        XDG_SESSION_TYPE = getenv('XDG_SESSION_TYPE')
        if XDG_SESSION_TYPE == 'wayland':
            environ['QT_QPA_PLATFORM'] = 'wayland'
        elif XDG_SESSION_TYPE is None:
            environ['QT_QPA_PLATFORM'] = 'xcb'

    application = QtWidgets.QApplication(sys.argv)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(f'{APPLICATION_NAME}.desktop')

    window = MainWindow(application=application)
    window.show_window()

    sys.exit(application.exec())
