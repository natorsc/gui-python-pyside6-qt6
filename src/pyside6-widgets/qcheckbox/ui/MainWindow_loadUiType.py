# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QCheckBox() com loadUiType()."""

from pathlib import Path

from PySide6 import QtCore, QtUiTools, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
UI_FILE = str(BASE_DIR.joinpath('MainWindow.ui'))

UiMainWindow, BaseQMainWindow = QtUiTools.loadUiType(UI_FILE)


class MainWindow(BaseQMainWindow, UiMainWindow):
    checkboxes = []

    def __init__(self, application):
        super().__init__()
        self.application = application
        self.setupUi(self)

        self.action_exit.triggered.connect(self.on_action_exit_clicked)

        self.button_group_01.buttonClicked.connect(self.on_button_clicked)

        self.checkbox_item_yes.stateChanged.connect(self.on_state_changed)

        self.checkbox_item_01.stateChanged.connect(
            lambda: self.on_state_changed_lambda(self.checkbox_item_01),
        )
        self.checkbox_item_02.stateChanged.connect(
            lambda: self.on_state_changed_lambda(self.checkbox_item_02),
        )
        self.checkbox_item_03.stateChanged.connect(
            lambda: self.on_state_changed_lambda(self.checkbox_item_03),
        )

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def on_button_clicked(self, radio_button):
        radio_button_text = radio_button.text()
        print(f'Texto do checkbox: {radio_button_text}.')
        radio_button_object_name = radio_button.objectName()
        print(f'Nome do objecto: {radio_button_object_name}.')
        if radio_button_object_name == 'male':
            print(f'Faça algo específico com checkbox {radio_button_text}.')
        elif radio_button_object_name == 'female':
            print(f'Faça algo específico com checkbox {radio_button_text}.')

    def on_state_changed(self, state):
        if state == QtCore.Qt.CheckState.Checked:
            print('Checkbox está MARCADO')
        else:
            print('Checkbox está DESMARCADO')

    def on_state_changed_lambda(self, checkbox):
        if checkbox.isChecked():
            self.checkboxes.append(checkbox)
        else:
            self.checkboxes.remove(checkbox)
        print(f'Checkboxes que estão na lista: {self.checkboxes}')


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
