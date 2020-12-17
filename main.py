import pyttsx3
import PyPDF2

reader = open('readingbook.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(reader)
pages = pdfReader.numPages
print(pages)
speaker = pyttsx3.init()
x=input('Enter page no. from where you want to start: ')
x=int(x)
for num in range(x-1, pages):
    page = pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
