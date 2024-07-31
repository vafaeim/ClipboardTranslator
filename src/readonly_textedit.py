import pyperclip
import re
import unicodedata
from googletrans import Translator as GoogleTranslator
from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from nltk.tokenize import word_tokenize
from custom_scrollbar import CustomScrollBar

class ReadOnlyTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setStyleSheet("""
            QTextEdit {
                background-color: #222222;
                color: #ffffff;
                border: 1px solid #555555;
                padding: 10px;
                font-family: Amiri;
                font-size: 17px;
            }
        """)
        self.translator = GoogleTranslator()
        self.last_copied_text = ""

        self.setVerticalScrollBar(CustomScrollBar())

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_A and event.modifiers() & Qt.ControlModifier:
            super().keyPressEvent(event)
        else:
            event.ignore()

    def mousePressEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            self.copy()
        else:
            event.ignore()

    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def contextMenuEvent(self, event):
        event.ignore()

    @staticmethod
    def normalize_text(text):
        text = text.lower()
        text = unicodedata.normalize('NFKD', text)
        text = re.sub(r'[^a-zA-Z0-9\s.,!?]', '', text)  # Keep .,!? and remove other special characters
        text = re.sub(r'\s+', ' ', text).strip()  # Collapse multiple spaces
        return text

    @staticmethod
    def tokenize_text(text):
        return ' '.join(word_tokenize(text))

    def updateTranslation(self):
        temp = pyperclip.paste()

        if temp != self.last_copied_text:
            self.last_copied_text = temp
            current_copied_text = temp.strip().replace('\n', ' ')
            current_copied_text = self.normalize_text(current_copied_text)
            current_copied_text = self.tokenize_text(current_copied_text)
            if len(current_copied_text) < 5001:
                translated = self.translator.translate(current_copied_text, dest='fa').text
                self.setPlainText(translated)
            else:
                self.setPlainText("متن شما خیلی طولانی است. (حداکثر 5 هزار نویسه)")
            del current_copied_text
