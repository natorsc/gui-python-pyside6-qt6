# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QToolBar()."""

from pathlib import Path

from PySide6 import QtGui, QtWidgets

HOME_DIR = Path.home()

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
ICONS_DIR = SRC_DIR.joinpath('data', 'icons')
ICONS = {
    'copy': str(ICONS_DIR.joinpath('copy.svg')),
    'exit': str(ICONS_DIR.joinpath('exit.svg')),
    'info': str(ICONS_DIR.joinpath('info.svg')),
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
        self.setWindowTitle('Python e Qt 6: PySide6 QToolBar()')
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

        toolbar = self.addToolBar('nome-da-barra')

        action_copy = QtGui.QAction(QtGui.QIcon(ICONS['copy']), 'Copiar', self)
        action_copy.triggered.connect(self.on_action_copy_clicked)
        toolbar.addAction(action_copy)

        # Definindo ícone com base no tema do sistema operacional.
        action_cut = QtGui.QAction('Recortar', self)
        # Se o ícone não existir o texto nome do ícone será exibido.
        action_cut.setIcon(QtGui.QIcon().fromTheme('edit-cut'))
        action_cut.triggered.connect(self.on_action_cut_clicked)
        toolbar.addAction(action_cut)

        action_about_qt = QtGui.QAction(
            QtGui.QIcon(ICONS['info']), 'Sobre o Qt', self)
        # Ação que é realizada quando o menu é clicado.
        action_about_qt.triggered.connect(self.on_action_about_qt_clicked)
        toolbar.addAction(action_about_qt)

        exit_app_action = QtGui.QAction(
            QtGui.QIcon(ICONS['exit']), 'Sair', self)
        exit_app_action.triggered.connect(self.on_action_exit_clicked)
        toolbar.addAction(exit_app_action)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def on_action_copy_clicked(self):
        print('Copiar')

    def on_action_cut_clicked(self):
        print('Recortar')

    def on_action_about_qt_clicked(self):
        self.application.aboutQt()


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
