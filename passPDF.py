#code by cyperom
#This python code will allow you to protect your PDF's with password with a click of a button. 
import PyPDF2
import os

files =[] # list

for file in os.listdir():
    if(file.endswith('.pdf')):
       files.append(file)

print(files)
for file in os.listdir():

    pdf_in_file = open(file,'rb')

    inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    pages_no = inputpdf.numPages
    output = PyPDF2.PdfFileWriter()

    for i in range(pages_no):
        inputpdf = PyPDF2.PdfFileReader(pdf_in_file)
    
    output.addPage(inputpdf.getPage(i))
    output.encrypt('cyperom') #you can change the password (cyperom) to any password you want 

    with open("password"+file, "wb") as outputStream:  #you can rename your file by replacing the ("password"+file) to anything you want but if you are protecting multible files make sure you replace it with something dynamic 
        output.write(outputStream)

    pdf_in_file.close()

#code by cyperom
