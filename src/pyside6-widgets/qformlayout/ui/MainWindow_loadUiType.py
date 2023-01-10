# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QFormLayout() com loadUiType()."""

from pathlib import Path

from PySide6 import QtUiTools, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
UI_FILE = str(BASE_DIR.joinpath('MainWindow.ui'))

UiMainWindow, BaseQMainWindow = QtUiTools.loadUiType(UI_FILE)


class MainWindow(BaseQMainWindow, UiMainWindow):

    def __init__(self, application):
        super().__init__()
        self.application = application
        self.setupUi(self)

        self.action_exit.triggered.connect(self.on_action_exit_clicked)

        self.checkbox_show_pwd.stateChanged.connect(
            self.on_state_changed_show_pwd
        )

        self.button_login.clicked.connect(self.on_button_clicked)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def on_state_changed_show_pwd(self):
        echo_mode = self.line_edit_password.echoMode()
        if echo_mode == QtWidgets.QLineEdit.Password:
            self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.line_edit_password.setEchoMode(QtWidgets.QLineEdit.Password)

    def on_button_clicked(self, widget):
        print(f'Usuário: {self.line_edit_user.text()}.')
        print(f'Senha: {self.line_edit_password.text()}.')


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
