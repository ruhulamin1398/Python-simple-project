import PyPDF2 
import re
import os

from PyPDF2 import PdfFileReader, PdfFileWriter
if not os.path.exists(os.path.join("work","pdf","output")):
    os.makedirs(os.path.join("work","pdf","output"))
#///////////////////////////////////////////////////

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()
    for path in paths:
    	print(path)

    	if path.endswith(".pdf"):
	        pdf_reader = PdfFileReader(path)
	        print(path)
	        for page in range(pdf_reader.getNumPages()):
	            # Add each page to the writer object
	            pdf_writer.addPage(pdf_reader.getPage(page))

    # Write out the merged PDF
    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
#/////////////////////////////////////////////////////////////////////
	

#-----------------------------------------------------------------------------------

	a=list( os.listdir(os.path.join("work","pdf")) )
	for temp in range(len(a)):
		a[temp]=(os.path.join("work","pdf",a[temp]))



	merge_pdfs( a , output=(os.path.join("work","pdf","output","merged.pdf")))

#---------------------------------------------------------------	
	
