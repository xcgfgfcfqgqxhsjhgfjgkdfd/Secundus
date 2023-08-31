import PyPDF2

# Ouvrir le fichier PDF
pdf=input("Entrez le chemin d'accès : ")
pdf_file = open(pdf, 'rb')

# Lire le fichier PDF
pdf_reader = PyPDF2.PdfReader(pdf_file)


# Extraire le texte de la première page
#length
p=len(pdf_reader.pages)
print("number of pages : ", p) 


T=int(input("Entrez la page à afficher : (-1)"))
page = pdf_reader.pages[T]
print(page.extract_text((0,200)))

# Fermer le fichier PDF
pdf_file.close()