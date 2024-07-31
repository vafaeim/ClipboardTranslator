import sys
from PyQt5.QtWidgets import QApplication
from clipboard_translator_app import ClipboardTranslatorApp

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QMainWindow {
            background-color: #222222;
            color: #ffffff;
        }
        QTextEdit {
            background-color: #222222;
            color: #ffffff;
            border: 1px solid #555555;
            padding: 10px;
            font-family: Amiri;
            font-size: 17px;
        }
    """)
    clipboard_translator = ClipboardTranslatorApp()
    clipboard_translator.show()
    sys.exit(app.exec_())
