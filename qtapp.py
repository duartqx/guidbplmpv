from PyQt5 import QtCore, QtWidgets, QtGui
from mpv import MPV

import locale
import sys


class MainWindow(QtWidgets.QMainWindow):

    def _setCentral(self, widget: QtWidgets.QWidget) -> None:
        self.setCentralWidget(widget)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        locale.setlocale(locale.LC_NUMERIC, "C")

        self.fullscreen: bool = False

        self.setWindowTitle("PyQt5 Hello World - MPV")

        self.label = QtWidgets.QLabel("Hello World")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        # player_canvas = QtWidgets.QWidget(self)
        self.setCentralWidget(self.label)

        self.player = MPV(
            wid=str(int(self.label.winId())),
            input_default_bindings=True,
            input_vo_keyboard=True
        )

        @self.player.key_binding("q")
        def _(state, name, char):
            "Disables the 'q' keybind"
            self.player.stop()


        @self.player.key_binding("f")
        def _(state, name, char):
            if state.upper() != "D-":
                return

            if self.fullscreen:
                self.showNormal()
            else:
                self.showFullScreen()
            self.fullscreen = not self.fullscreen

        self.playbutton = QtWidgets.QPushButton("Play", self)
        self.playbutton.setFixedSize(200, 50)
        self.playbutton.clicked.connect(
            lambda: self.player.play("/home/duartqx/Media/Videos/[ASW] Kaijuu 8-gou - 01 [1080p HEVC][DCC2A44E].mkv")
        )

        layout = QtWidgets.QVBoxLayout(self.label)
        layout.addWidget(self.playbutton)
        layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout = lambda: layout


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec_())
