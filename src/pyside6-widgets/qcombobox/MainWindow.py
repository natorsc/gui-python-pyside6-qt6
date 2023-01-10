# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QComboBox()."""

from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
ICONS_DIR = SRC_DIR.joinpath('data', 'icons')
ICONS = {
    'exit': str(ICONS_DIR.joinpath('exit.svg')),
    'window': str(ICONS_DIR.joinpath('br.com.justcode.Example.png')),
}


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, application):
        super().__init__()
        self.application = application

        primary_screen = self.application.primaryScreen()
        primary_screen_geometry = primary_screen.geometry()
        primary_screen_height = primary_screen_geometry.height()
        primary_screen_width = primary_screen_geometry.width()

        window_width = int(primary_screen_width / 2)
        window_height = int(primary_screen_height / 2)

        self.setGeometry(0, 0, window_width, window_height)
        self.setMinimumSize(window_width, window_height)
        self.setMaximumSize(window_width + 200, window_height + 200)
        self.setWindowTitle('Python e Qt 6: PySide6 QComboBox()')
        self.setWindowIcon(QtGui.QIcon(ICONS['window']))

        menu_bar = self.menuBar()

        menu_file = menu_bar.addMenu(self.tr('Arquivo'))
        action_exit = QtGui.QAction(
            QtGui.QIcon(ICONS['exit']), self.tr('Sair'), self
        )
        action_exit.triggered.connect(self.on_action_exit_clicked)
        menu_file.addAction(action_exit)

        vbox = QtWidgets.QVBoxLayout()

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.label_result = QtWidgets.QLabel()
        self.label_result.setText('Este texto será alterado...')
        self.label_result.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(self.label_result)

        label = QtWidgets.QLabel()
        label.setText('Selecione um dos itens:')
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft |
                           QtCore.Qt.AlignmentFlag.AlignBottom)
        vbox.addWidget(label)

        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItem('Selecione.')
        for item in range(1, 4):
            self.combobox.addItem(f'Item {item}')

        # Outra forma de acionar novos itens.
        # Passando uma lista de itens.
        itens = ['Item 4', 'Item 5', 'Item 6']
        self.combobox.addItems(itens)

        # Conectando o sinal a um slot.
        self.combobox.currentIndexChanged.connect(
            self.on_current_index_changed)
        vbox.addWidget(self.combobox)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def on_current_index_changed(self, index):
        if index != 0:
            combobox_text = self.combobox.currentText()
            print(combobox_text)
            self.label_result.setText(combobox_text)


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
