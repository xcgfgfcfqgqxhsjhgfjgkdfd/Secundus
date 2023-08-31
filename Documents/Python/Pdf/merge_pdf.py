import PyPDF2

pdf_merger = PyPDF2.PdfMerger()
print("Pour fusionner une page, il faut entrer le nom de chaque pdf à lier, et le nombre de pdf à lier (+1).")
u=int(input("Entrez le nombre de pdf à lier : "))
i=1;

def Merge_PDF():
	a = input("Entrez le chemin absolu : ")
	b = open(a, 'rb')
	pdf_merger.append(b)

	return a,b


while i < u:
	Merge_PDF()
	i = i + 1


# Fusionne les fichiers PDF
ex=input("Entrez le nom du pdf final avec .pdf : ")
pdf_merger.write(ex)

# Fermeture des fichiers PDF
a.close()
