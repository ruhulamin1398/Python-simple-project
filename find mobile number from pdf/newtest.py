import PyPDF2 
import re
import os



# creating directory if they dont exist 
if not os.path.exists(os.path.join("work","pdf")):
    os.makedirs(os.path.join("work","pdf"))
 
#if not os.path.exists(os.path.join("/Users","CBL", "Desktop","chatrobondhu", "pdf")):
 #   os.makedirs(os.path.join("/Users","CBL", "Desktop","chatrobondhu", "pdf"))


phoneNumRegex = re.compile(r'01\d\d\d\d\d\d\d\d\dCERTIFICATE')
file=open("pdflist.txt","w")

#ruhul=open("ruhul.txt","w")


for f in os.listdir(os.path.join("work","pdf")):
    if f.endswith(".pdf"):
        file.write(os.path.join("work","pdf", f))
        file.write(os.path.join('\n'))

		
		

file=open("pdflist.txt","r")
contents =file.readlines()
# phonefile=open("Desktop/phone.txt","w+")
phonefile=open(os.path.join("work","phone.txt"), "w+")
for i in contents:
	a=len(str(i))-1
	pdfname=i[:a:]
	pdfname=os.path.join("",pdfname)
	print("Searching on  "+pdfname+".  . . . . . . . . . . . . . ")
	pdfFileObj = open(str(pdfname), 'rb') 
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
	pageNumber= pdfReader.numPages

	for i in range(pageNumber):	 
		pageObj = pdfReader.getPage(i) 
#		ruhul.write(pageObj.extractText())
		mo = phoneNumRegex.search(((pageObj.extractText())))
		print(pageObj.extractText())
		phonefile.write(mo.group()[:11]+"\n")



	
phonefile.close()	
file.close()
pdfFileObj.close() 
