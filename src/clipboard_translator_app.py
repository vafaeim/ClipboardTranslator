from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QDesktopWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon
from readonly_textedit import ReadOnlyTextEdit

class ClipboardTranslatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CliTrans v1.0.0")
        self.setGeometry(0, 0, 320, 140)
        self.setWindowIcon(QIcon('./img/icon.ico'))

        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QVBoxLayout(self.centralWidget)

        self.textEdit = ReadOnlyTextEdit(self)
        self.layout.addWidget(self.textEdit)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.textEdit.updateTranslation)
        self.timer.start(1000)

        self.setWindowFlags(self.windowFlags() | Qt.WindowStaysOnTopHint)

        self.adjustPosition()

    def adjustPosition(self):
        screen = QDesktopWidget().screenGeometry()
        screen_width = screen.width()
        n = 20
        self.move(screen_width - self.width() - n, n)

    def closeEvent(self, event):
        self.timer.stop()
        event.accept()
