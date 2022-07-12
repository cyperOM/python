import PyPDF2
import os

files =[] # list

for file in os.listdir():
    if(file.endswith('.pdf')):
       files.append(file)

print(files)
for file in os.listdir():

#pdf_in_file = open("simple.pdf",'rb')
    pdf_in_file = open(file,'rb')

    inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    pages_no = inputpdf.numPages
    output = PyPDF2.PdfFileWriter()

    for i in range(pages_no):
        inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt('cyperom')

    #with open("simple_password_protected.pdf", "wb") as outputStream:
    with open("password"+file, "wb") as outputStream:
        output.write(outputStream)

    pdf_in_file.close()

#code by cyperom