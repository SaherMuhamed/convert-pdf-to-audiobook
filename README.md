# PDF to Audiobook Converter
This Python script converts a PDF file into an audiobook by extracting the text from the PDF and converting it to speech using the gTTS (Google Text-to-Speech) library.

## Prerequisites
Make sure you have the following libraries installed:
  - `PyPDF2` library
  - `gTTS` (Google Text-to-Speech) library

You can install these libraries using `pip` command:
```commandline
pip install PyPDF2 gTTS
```

## Usage
1. Place the PDF file you want to convert in the same directory as the script.
2. Open the script in a Python editor or IDE.
3. Modify the `pdf_file_path` variable to specify the name of your PDF file.
4. Run the script.

## Features
- **Extract text from PDF files:** The project allows users to extract the text content from PDF files, enabling further processing and conversion to speech.
- **Text-to-speech conversion:** The extracted text is converted into speech using the gTTS library, generating an audio representation of the PDF content.
- **Audiobook generation:** The converted speech is saved as an MP3 file, creating an audiobook version of the PDF that users can listen to at their convenience.
- **User-friendly interface:** The project can be executed through a command-line interface, making it accessible and straightforward for users to convert PDF files into audiobooks.

The script will extract the text from the PDF file and convert it to an audiobook. The resulting audiobook will be saved in the same directory with the same name as the PDF file but with the `.mp3` extension.

**Note:** Please ensure that you have the necessary permissions to convert the PDF file into an audiobook, and respect any copyright restrictions that may apply.

Feel free to customize the script according to your requirements and preferences.
