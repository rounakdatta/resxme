from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

from nltk.tokenize import sent_tokenize

def scrape_pdf(pdfname):

    # initial essentials
    rsrcmgr = PDFResourceManager()
    sio = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    # extract text
    f = open(pdfname, 'rb')
    for page in PDFPage.get_pages(f):
        interpreter.process_page(page)
    f.close()

    text = sio.getvalue()
    device.close()
    sio.close()

    return text