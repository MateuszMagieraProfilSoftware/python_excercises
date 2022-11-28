from pprint import pprint
import PyPDF2

with open('/home/mateusz/Downloads/Report.pdf','rb') as pdf_report:
    read_pdf = PyPDF2.PdfFileReader(pdf_report)
    number_of_pages = read_pdf.getNumPages()
    page = read_pdf.pages[5]
    page_content = page.extractText()


pprint(page_content)