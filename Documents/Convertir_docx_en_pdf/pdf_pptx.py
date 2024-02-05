import subprocess
from pathlib import Path
import os

#Ce fichier permet la conversion de document .pdf en .pptx, et le fichier de conversion et le .pdf peuvent ne pas être dans le même répertoire.
#Par contre le fichier convertit sera dans le même répertoire que le fichier de conversion. 
pdf2pptx = "pdf2pptx" 


t = input("Entrez le répertoire contenant votre fichier à convertir : \n")

#Cette boucle sert à montrer tous les fichiers d'un répertoire. Il ne reste plus qu'à faire un crtl+c et ctrl+v.
root = t
for path, subdirs, files in os.walk(t):
    for name in files:
        print(os.path.join(path, name))

name = input("Entrez le nom du fichier.pdf, et avec tout le répertoire s'il est pas dans le dossier du convertisseur : \n")
print("-o ??.pptx, avec le nom de votre choix pour ??")
output = input("Entrez le nom proposé ci-dessus : \n")

list_files = subprocess.run([pdf2pptx, name, output])

print("conversion effectuée avec succès !")