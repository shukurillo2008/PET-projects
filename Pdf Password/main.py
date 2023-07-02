from PyPDF2 import PdfFileWriter, PdfFileReader,PdfReader, PdfWriter
from getpass import getpass

file = input("Pdf file --> ")
password = getpass(prompt='Password --> ')

def add_password_pdf(file, password):
    pdf = PdfReader(file)
    pdfwriter = PdfWriter()
    for page in range(len(pdf.pages)):
        pdfwriter.add_page(pdf.pages[page])
    pdfwriter.encrypt(password)

    with open(f'{file}', 'wb') as file:
        return pdfwriter.write(file)


add_password_pdf(file, password)


    
