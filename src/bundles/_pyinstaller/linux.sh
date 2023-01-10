pyinstaller \
--noconfirm \
--log-level=WARN \
--windowed \
--name "br.com.justcode.Example" \
--add-data="ui:ui" \
--add-data="data:data" \
--upx-dir=/usr/local/share/ \
MainWindow.py