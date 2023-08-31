from pypdf import PdfReader, PdfWriter
from pathlib import Path

print("Pour extraire une page, il faut entrer le nom du pdf ou il faut extraire, le numero de la page pour la serie.")
u=int(input("Entrez le nombre de pdf (+1) devant faire l'objet d'extraction : "))
o=(int(input("entrez le numero (-1) de la page à extraire : ")))
i=1;
t=input("entrez un chemin : ")
print(Path(t))


def extract_PDF():
	"""Takes an input of a path for a pdf file, and then a letter. """
	a=input("Input avec .pdf : ")
	c=input("Une lettre : ")
	
	reader = PdfReader(a)
	p = reader.pages[o]	
	
	"""Create a pdfReader that takes the name of the path, and then read the selected page indicated with the o.""" 
	
	writer = PdfWriter()
	writer.add_page(p)
	
	"""Create a pdfWriter, and the page selected is added to the writer"""
	
	b=Path((a)+c+".pdf")
	print(b)
	
	"""Create a path for the file created with the pages extracted from the pdf file, and show the path. 
	Finaly, write the pdf file with extracted pages."""

	writer.write(b)

	

while i<u:
	extract_PDF()
	i = i + 1 



print("Function name : ", extract_PDF.__name__)
print(extract_PDF.__doc__)


