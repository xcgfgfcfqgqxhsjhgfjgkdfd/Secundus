import os
import win32com.client

wdFormatPDF = 17

path1=input("Entrez le chemin d'accès absolu du fichier en entrée .docx")
path2=input("Entrez le chemin absolu du fichier en sortie .pdf")
inputFile = os.path.abspath(path1)
outputFile = os.path.abspath(path2)
word = win32com.client.Dispatch('Word.Application')
doc = word.Documents.Open(inputFile)
doc.SaveAs(outputFile, FileFormat=wdFormatPDF)
doc.Close()
word.Quit()