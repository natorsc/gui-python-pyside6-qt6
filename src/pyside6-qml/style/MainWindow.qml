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
    title: 'Python e Qt 6: PySide6 QML Styles'
    ColumnLayout {
        id: column
        anchors.fill: parent
        anchors.margins: 24
        spacing: 12
        TextField {
            id: text_field
            placeholderText: qsTr('Digite algo.')
            Layout.alignment: Qt.AlignTop
            Layout.fillWidth: true
        }
        Text {
            id: label
            Layout.alignment: Qt.AlignVCenter | Qt.AlignHCenter
            text: qsTr('Esse texto será alterado ao clicar no botão.')
        }
        Button {
            id: button
            Layout.alignment: Qt.AlignHCenter | Qt.AlignBottom
            text: qsTr('Clique aqui')
            onClicked: {
                label.text = mainwindow.on_button_clicked(text_field.text)
            }
        }
    }
}
