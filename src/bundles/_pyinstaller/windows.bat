pyinstaller
--noconfirm ^
--log-level=WARN ^
--windowed ^
--name "br.com.justcode.Example" ^
--add-data="ui:ui" ^
--add-data="data:data" ^
--icon=data\icons\app-icon.ico ^
MainWindow.py