from PyPDF2 import*

myFile = input("Entrez le chemin d'accès : ")	
document = PdfReader(open(myFile, 'rb'))

meta = document.metadata

# All of the following could be None!
print("author : ", meta.author)
print("creator : ", meta.creator)
print("producer : ", meta.producer)
print("subject : ", meta.subject)
print("title : ", meta.title)
