# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QTranslator()."""

from pathlib import Path

from PySide6 import QtCore, QtGui, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR.parent.parent
ICONS_DIR = SRC_DIR.joinpath('data', 'icons')
ICONS = {
    'exit': str(ICONS_DIR.joinpath('exit.svg')),
    'window': str(ICONS_DIR.joinpath('br.com.justcode.Example.png')),
}
LANGS_DIR = BASE_DIR.joinpath('locales')

HOME_DIR = Path.home()


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

        self.setWindowTitle(
            self.application.translate(
                'window_title',
                'Python e Qt 6: PySide6 QTranslator() e translate.',
            ),
        )

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

        label = QtWidgets.QLabel()
        label.setText(
            self.application.translate(
                'label',
                'Após trocar o idioma é necessário reiniciar o aplicativo.',
            ),
        )
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        vbox.addWidget(label)

        self.combobox = QtWidgets.QComboBox()
        self.combobox.addItem(
            self.application.translate(
                'combobox',
                'Selecione um idioma.',
            ),
        )
        self.combobox.addItem('en_US')
        self.combobox.addItem('pt_BR')
        self.combobox.setCurrentText(app_settings.value('language'))
        self.combobox.currentIndexChanged.connect(self.set_translate)
        vbox.addWidget(self.combobox)

    def showEvent(self, event):
        print(f'Janela aberta: {event}')

    def focusInEvent(self, event):
        print(f'Janela ganhou foco: {event}')

    def closeEvent(self, event):
        print(f'Janela fechada: {event}')

    def on_action_exit_clicked(self):
        self.application.quit()

    def set_translate(self, index):
        combobox_text = self.combobox.currentText()
        if index != 0:
            if combobox_text == 'pt_BR':
                app_settings.setValue('language', 'default')
            else:
                app_settings.setValue('language', f'{combobox_text}')


if __name__ == "__main__":
    import sys

    APPLICATION_NAME = 'br.com.justcode.Example'
    ORGANIZATION_NAME = APPLICATION_NAME.split('.')[2]
    ORGANIZATION_DOMAIN = '.'.join(APPLICATION_NAME.split('.')[0:3])

    app_settings = QtCore.QSettings(ORGANIZATION_NAME, APPLICATION_NAME)

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

    CONF_FILE = HOME_DIR.joinpath(
        '.config',
        ORGANIZATION_NAME,
        f'{APPLICATION_NAME}.conf',
    )
    print(f'{APPLICATION_NAME}.qm')
    if CONF_FILE.exists():
        translator = QtCore.QTranslator()
        translator.load(
            str(
                LANGS_DIR.joinpath(
                    f'{app_settings.value("language")}',
                    'LC_MESSAGES',
                    f'{APPLICATION_NAME}.qm',
                ),
            ),
        )
    else:
        system_locale = QtCore.QLocale()

        translator = QtCore.QTranslator()
        translator.load(
            str(
                LANGS_DIR.joinpath(
                    f'{system_locale.name()}',
                    'LC_MESSAGES',
                    f'{APPLICATION_NAME}.qm',
                ),
            ),
        )
    application.installTranslator(translator)

    window = MainWindow(application=application)
    window.show()

    sys.exit(application.exec())
