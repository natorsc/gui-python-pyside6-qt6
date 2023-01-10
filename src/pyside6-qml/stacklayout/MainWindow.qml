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
    title: 'Python e Qt 6: PySide6 QML StackLayout{}'
    footer: TabBar {
        id: tabbar
        width: parent.width
        TabButton {
            text: qsTr('Tela 01')
        }
        TabButton {
            text: qsTr('Tela 02')
        }
        TabButton {
            text: qsTr('Tela 03')
        }
    }
    StackLayout {
        id: stacklayout
        currentIndex: tabbar.currentIndex
        anchors.centerIn: parent
        anchors.fill: parent
        Item {
            id: item01
            Text {
                text: qsTr('Tela 01')
                anchors.centerIn: parent
            }
        }
        Item {
            id: item02
            Text {
                text: qsTr('Tela 02')
                anchors.centerIn: parent
            }
        }
        Item {
            id: item03
            Text {
                text: qsTr('Tela 03')
                anchors.centerIn: parent
            }
        }
    }
}
