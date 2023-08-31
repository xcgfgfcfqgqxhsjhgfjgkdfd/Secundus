from pypdf import PdfReader, PdfWriter



U=int(input("Entrez un entier entre 1 et 10, 10 compris. Cet entier est le nombre de pages à extraire du PDF."))
i=1;
t=input("Entrez le chemin d'accès avec .pdf : ")
reader = PdfReader(t)

def E_PDF(t):
	a = int(input("Entrez le numero de la page à extraire"))
	p = reader.pages[a]
	writer = PdfWriter()
	writer.add_page(p)

	return a, t

while i < U :
	E_PDF(t)
	i = i + 1


u=input("Entrez le chemin en sortie avec .pdf : ")
writer.write(u)

