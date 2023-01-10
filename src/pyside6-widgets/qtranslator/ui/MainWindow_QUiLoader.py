# -*- coding: utf-8 -*-
"""Python e Qt 6: PySide6 QTranslator() com QUiLoader()."""

from pathlib import Path

from PySide6 import QtCore, QtUiTools, QtWidgets

BASE_DIR = Path(__file__).resolve().parent
UI_FILE = str(BASE_DIR.joinpath('MainWindow.ui'))
LANGS_DIR = BASE_DIR.joinpath('locales')
HOME_DIR = Path.home()


class MainWindow(QtCore.QObject):

    def __init__(self, application):
        super().__init__()
        self.application = application

        loader = QtUiTools.QUiLoader()
        self.ui = loader.load(UI_FILE)

        self.ui.action_exit.triggered.connect(self.on_action_exit_clicked)

        self.ui.combobox
        self.ui.combobox.setCurrentText(app_settings.value('language'))
        self.ui.combobox.currentIndexChanged.connect(self.set_translate)

    def on_action_exit_clicked(self):
        self.application.quit()

    def show_window(self):
        self.ui.show()

    def set_translate(self, index):
        combobox_text = self.ui.combobox.currentText()
        if index != 0:
            if combobox_text == 'pt_BR':
                app_settings.setValue('language', 'default')
            else:
                app_settings.setValue('language', f'{combobox_text}')


if __name__ == "__main__":
    import sys

    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

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
    window.show_window()

    sys.exit(application.exec())
