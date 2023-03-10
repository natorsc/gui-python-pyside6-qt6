# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QFileDialog() arquivo(s)."""

from pathlib import Path

from PySide6 import QtGui, QtWidgets

HOME = str(Path.home())
BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
ICONS_DIR = SRC_DIR.joinpath('data', 'icons')
ICONS = {
    'exit': str(ICONS_DIR.joinpath('exit.svg')),
    'window': str(ICONS_DIR.joinpath('br.com.justcode.Example.png')),
}

# Filtros.
MINE_TYPE_FILTERS = ['image/jpeg', 'image/png', 'image/gif', 'image/bmp',
                     'application/octet-stream']
FILTERS = ('JPEG image (*.jpg *.jpeg *.jpe);;PNG image (*.png);;'
           'GIF image (*.gif);;Windows BMP image (*.bmp);;All files (*.*)')


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
        self.setWindowTitle('Python e Qt 6: PySide6 QFileDialog() arquivo(s)')
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

        push_button = QtWidgets.QPushButton()
        push_button.setText('Clique Aqui!')
        push_button.clicked.connect(self.on_button_clicked)
        vbox.addWidget(push_button)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def on_button_clicked(self):
        file_dialog = QtWidgets.QFileDialog(self)

        # [!] M??todo 1 [!].
        # Adicionando filtro com base no mine_type.
        # file_dialog.setMimeTypeFilters(MINE_TYPE_FILTERS)

        # Seleciona 1 arquivo.
        # file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        # Seleciona multiplos arquivos.
        # file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)

        # Verificando a resposta do dialogo.
        # if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
        #    print(f'Arquivo(s) selecionado(s): {file_dialog.selectedFiles()}')
        #    print(f'Mime type do filtro: {file_dialog.selectedMimeTypeFilter()}')
        #    print(f'Nome do filtro: {file_dialog.selectedNameFilter()}')

        # [!] M??todo 2 [!].
        # Seleciona 1 arquivo.
        file, filter = file_dialog.getOpenFileName(
            parent=self,
            caption='',
            dir=HOME,
            filter=FILTERS,
            selectedFilter='',
            # Apenas para exemplificar.
            # options=QtWidgets.QFileDialog.Option.DontUseNativeDialog,
        )

        # Seleciona multiplos arquivos.
        # file, filter = file_dialog.getOpenFileNames(
        #    self,
        #    '',
        #    '',
        #    FILTERS,
        #    '',
        # )
        if file:
            print(f'Arquivo(s) selecionado(s): {file}')
            print(f'Mime type do filtro: {filter}')


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
