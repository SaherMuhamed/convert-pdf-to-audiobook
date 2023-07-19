import PyPDF2
from gtts import gTTS


def extract_text_from_pdf(pdf_file):
    try:
        with open(pdf_file, mode='rb') as file:
            # Create a PDF reader object
            pdf_reader = PyPDF2.PdfReader(file)

            # Initialize an empty string to store the extracted text
            extracted_pdf_text = ""

            # Loop through each page in the PDF
            for page_num in range(len(pdf_reader.pages)):
                # Get the page object
                page = pdf_reader.pages[page_num]

                # Extract the text from the page and append it to the extracted_text variable
                extracted_pdf_text += page.extract_text()

            return extracted_pdf_text

    except FileNotFoundError:
        print(f"Error: The file '{pdf_file}' was not found.")
        return None


pdf_file_path = "cover-1.pdf"
extracted_text = extract_text_from_pdf(pdf_file=pdf_file_path)
if extracted_text:
    tts = gTTS(extracted_text)
    if tts:
        tts.save(f'{pdf_file_path.split(".pdf")[0]}.mp3')
        print(f"[+] Your pdf {pdf_file_path} is converted to an audiobook successfully")
    # print(extracted_text)
