# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QTabWidget()."""

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
        self.setWindowTitle('Python e Qt 6: PySide6 QTabWidget()')
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

        tab_widget = QtWidgets.QTabWidget()
        vbox.addWidget(tab_widget)

        # Abra 01.
        tab_01_layout = QtWidgets.QVBoxLayout()

        tab_01 = QtWidgets.QWidget()
        tab_01.setLayout(tab_01_layout)
        tab_widget.addTab(tab_01, 'Aba 01')

        label_tab_01 = QtWidgets.QLabel()
        label_tab_01.setText('Aba 01')
        label_tab_01.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label_tab_01.setStyleSheet(
            'QLabel {background-color: #B3E5FC; color: black;}'
        )
        tab_01_layout.addWidget(label_tab_01)

        # Abra 02.
        tab_02_icon = QtGui.QIcon(ICONS['window'])

        tab_02_layout = QtWidgets.QVBoxLayout()

        tab_02 = QtWidgets.QWidget()
        tab_02.setLayout(tab_02_layout)
        tab_widget.addTab(tab_02, tab_02_icon, 'Aba 02')

        label_tab_02 = QtWidgets.QLabel()
        label_tab_02.setText('Aba 02')
        label_tab_02.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label_tab_02.setStyleSheet(
            'QLabel {background-color: #C8E6C9; color: black;}'
        )
        tab_02_layout.addWidget(label_tab_02)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()


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
