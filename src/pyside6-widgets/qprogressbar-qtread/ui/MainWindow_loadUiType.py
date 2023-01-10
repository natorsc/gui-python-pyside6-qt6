# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QProgressBar() e QThread() com loadUiType()."""

from pathlib import Path
from time import sleep

from PySide6 import QtCore, QtUiTools, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
UI_FILE = str(BASE_DIR.joinpath('MainWindow.ui'))

UiMainWindow, BaseQMainWindow = QtUiTools.loadUiType(UI_FILE)


class Thread(QtCore.QThread):
    # Nome do signal (sinal) que será emitido.
    signal_name = QtCore.Signal(int)

    def __init__(self):
        super(Thread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # Operação que será realizada na tread.
        for value in range(101):
            sleep(0.1)
            # Emitindo o signal e passando o valor.
            self.signal_name.emit(value)


class MainWindow(BaseQMainWindow, UiMainWindow):

    def __init__(self, application):
        super().__init__()
        self.application = application
        self.setupUi(self)

        self.action_exit.triggered.connect(self.on_action_exit_clicked)

        self.progressbar.valueChanged.connect(self.on_progressbar_value_change)
        self.button.clicked.connect(self.on_button_clicked)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def on_button_clicked(self):
        self.thread = Thread()
        self.thread.signal_name.connect(self.start_tread)
        self.thread.start()
        self.button.setEnabled(False)

    def on_progressbar_value_change(self, value):
        print(f'Valor do QProgressBar: {value}.')

    def start_tread(self, value):
        self.progressbar.setValue(int(value))
        if self.progressbar.value() == 100:
            self.progressbar.setValue(0)
            self.button.setEnabled(True)
            self.thread.quit()
            del self.thread


if __name__ == "__main__":
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

    application = QtWidgets.QApplication(sys.argv)
    application.setOrganizationName(ORGANIZATION_NAME)
    application.setOrganizationDomain(ORGANIZATION_DOMAIN)
    application.setApplicationName(APPLICATION_NAME)
    application.setDesktopFileName(f'{APPLICATION_NAME}.desktop')

    window = MainWindow(application=application)
    window.show()

    sys.exit(application.exec())