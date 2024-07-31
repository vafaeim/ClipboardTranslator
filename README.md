# Clipboard Translator

Clipboard Translator is a PyQt5-based desktop application that monitors the clipboard for text and translates it into Persian using the Google Translate API. This application is designed for real-time translation, providing users with immediate translations of copied text.

## Features

- **Automatic Clipboard Monitoring:** The application continuously monitors the clipboard for new text.
- **Real-time Translation:** Translates the copied text into Persian instantly.
- **Custom Styling:** Modern and minimalistic UI design with custom scrollbar and text editor styles.
- **Text Normalization:** Converts text to lowercase, removes special characters, and tokenizes text before translation.
- **Persian Translation:** Utilizes Google Translate to translate text into Persian.

## Installation

### Prerequisites

- Python 3.6 or higher
- Git

### Setup Instructions

1. **Clone the repository:**
   ```sh
   git clone https://github.com/vafaeim/ClipboardTranslator.git
   cd ClipboardTranslator
   ```

2. **Create a virtual environment and activate it:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Download NLTK 'punkt' package:**
   ```sh
   python -m nltk.downloader punkt
   ```

5. **Run the application:**
   ```sh
   python src/main.py
   ```

## Project Structure

```
ClipboardTranslator/
├── img/
│   └── icon.ico
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── custom_scrollbar.py
│   ├── readonly_textedit.py
│   ├── clipboard_translator_app.py
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

### Files Description

- **src/main.py:** Entry point of the application.
- **src/custom_scrollbar.py:** Contains the `CustomScrollBar` class for custom scrollbar styling.
- **src/readonly_textedit.py:** Contains the `ReadOnlyTextEdit` class for custom text editing and translation.
- **src/clipboard_translator_app.py:** Contains the `ClipboardTranslatorApp` class for the main application window.
- **img/icon.ico:** Icon used for the application window.
- **README.md:** Project documentation.
- **requirements.txt:** List of Python dependencies.
- **LICENSE:** License information.
- **.gitignore:** Specifies files and directories to be ignored by git.

## Usage

1. **Run the Application:**
   ```sh
   python src/main.py
   ```

2. **Copy Text to Clipboard:**
   - Copy any text from any application (e.g., a web browser, text editor).

3. **View Translated Text:**
   - The Clipboard Translator window will display the translated text in Persian.

## Dependencies

- **PyQt5:** Python bindings for Qt libraries, used for creating the GUI.
- **googletrans==4.0.0-rc1:** Google Translate API for translating text.
- **pyperclip:** A cross-platform clipboard module for Python.
- **nltk:** Natural Language Toolkit, used for text tokenization.

Install the dependencies using:
```sh
pip install -r requirements.txt
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes. Ensure your code adheres to the existing style and includes appropriate tests.

## Acknowledgements

- [PyQt5](https://pypi.org/project/PyQt5/)
- [googletrans](https://pypi.org/project/googletrans/)
- [pyperclip](https://pypi.org/project/pyperclip/)
- [nltk](https://pypi.org/project/nltk/)

## Contact

For any inquiries or issues, please contact [vafaeim@icloud.com](mailto:vafaeim@icloud.com).

---

Thank you for using Clipboard Translator!
