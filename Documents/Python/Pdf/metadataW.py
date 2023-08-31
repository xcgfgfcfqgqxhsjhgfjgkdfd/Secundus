from datetime import datetime
from pypdf import PdfReader, PdfWriter

U=input("Entrez le chemin d'accès : ")
reader = PdfReader(U)
writer = PdfWriter()

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# If you want to add the old metadata, include this line
metadata = reader.metadata
writer.add_metadata(metadata)

# Add the new metadata
W=input("nom de l'ateur : ")
P=input("Le producteur (logiciel) : ")
T=input("Titre de l'oeuvre : ")
S=input("Le sujet : ")
C=input("Le créateur : ")
writer.add_metadata(
    {
        "/Author": W,
        "/Producer": P,
        "/Title": T,
        "/Subject": S,
        "/Creator": C,     
    }
)

# Save the new PDF to a file
E=input("Entrez le chemin du fichier en sortie : ")
with open(E, "wb") as f:
    writer.write(f)