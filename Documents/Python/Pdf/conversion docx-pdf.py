from docx2pdf import convert

print("Pour entrer le nom du fichier, s'il est dans un autre répertoire, pensez à mettre le chemin d'accès complet")
inputFile = input("Entrez le nom du fichier word en entrée, avec le .docx : ")
outputFile = input("Entrez le nom du fichier pdf en sortie, avec le .pdf : ")

convert(inputFile, outputFile)

print("conversion effectuée avec succès !")