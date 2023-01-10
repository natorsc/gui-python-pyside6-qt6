import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

ApplicationWindow {
    id: app
    visible: true
    x: 40
    y: 50
    width: Screen.width / 2
    height: Screen.height / 2
    title: 'Python e Qt 6: PySide6 QML ToolBar{}'
    header: ToolBar {
        RowLayout {
            anchors.fill: parent
            ToolButton {
                // Utilizando ícone com base no tema do sistema.
                // icon.name: 'application-exit'
                ToolTip.visible: hovered
                ToolTip.text: qsTr('Sair do aplicativo.')
                onClicked: Qt.quit()
                // Utilizando um ícone personalizado.
                Image {
                    id: image
                    source: '../../data/icons/exit.svg'
                    fillMode: Image.PreserveAspectFit
                    anchors.fill: parent
                    anchors.margins: 2
                }
            }
        }
    }
}
