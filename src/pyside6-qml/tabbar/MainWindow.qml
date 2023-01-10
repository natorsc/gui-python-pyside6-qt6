import QtQuick
import QtQuick.Controls

ApplicationWindow {
    id: app
    visible: true
    x: 40
    y: 50
    width: Screen.width / 2
    height: Screen.height / 2
    title: 'Python e Qt 6: PySide6 QML TabBar{}'
    footer: TabBar {
        width: parent.width
        TabButton {
            text: qsTr("Aba 01")
            onClicked: console.log('Botão pressionando')
        }
        TabButton {
            text: qsTr("Aba 02")
            onClicked: console.log('Botão pressionando')
        }
        // Loop de repetição.
        Repeater {
            model: ["Aba 03", "Aba 04"]
            TabButton {
                text: qsTr(modelData)
                onClicked: console.log('Botão pressionando')
            }
        }
    }
}
