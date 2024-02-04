from docx2pdf import convert
from pathlib import Path
import os


print("Pour que la conversion s'effectue, vous devez avoir placé vos fichiers à convertir dans le répertoire du fichier de conversion.")
u=int(input("Entrez le nombre de fichier à convertir : \n"))
t=input("entrez le répertoire contenant le fichier de conversion : \n")
i=0;
print(Path(t))
print("Le contenu du répertoire entré va être affiché.")

root = t
for path, subdirs, files in os.walk(t):
    for name in files:
        print(os.path.join(path, name))

def Word_to_PDF():
	"""Takes an input of a path, and then a letter. """
	a=input("Input avec .docx : \n")
	c=input("Le nom du pdf : \n")
	b=Path(c+".pdf")
	convert(a, b)


	i=0

while i<u:
	Word_to_PDF()
	i = i + 1 

print("Les fichiers en format pdf seront dans le répertoire du fichier de conversion.")
print("conversion effectuée avec succès !")