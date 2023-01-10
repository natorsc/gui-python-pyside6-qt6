import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: app
    visible: true
    x: 40
    y: 50
    width: Screen.width / 2
    height: Screen.height / 2
    title: 'Python e Qt 6: PySide6 QML menuBar{}'
    menuBar: MenuBar {
        Menu {
            title: qsTr('Arquivo')
            MenuItem {
                text: qsTr('Sair')
                // icon.name: "application-exit-rtl-symbolic"
                icon.source: "../../data/icons/exit.svg"
                onTriggered: Qt.quit()
            }
        }
    }
}
