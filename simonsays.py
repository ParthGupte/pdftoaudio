import pyttsx3
import PyPDF2
engine = pyttsx3.init()
f = open("C:\\Informatics Practices\\pdftoaudio\\digitalfortress.pdf","rb")
pdfReader = PyPDF2.PdfFileReader(f)
totalpages = pdfReader.getNumPages()
book = ''
for i in range(totalpages):
    pageobj = pdfReader.getPage(i)
    text = pageobj.extractText()
    book+=text
engine.setProperty('rate',150)
engine.save_to_file(book,'C:\\Informatics Practices\\pdftoaudio\\book1.mp3')
engine.runAndWait()