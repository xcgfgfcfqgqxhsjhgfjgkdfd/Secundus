import xlrd

Excel=input("Entrez le chemin d'accès du fichier Excel, avec le .xlsx : ")
document = xlrd.open_workbook(Excel)
print("Nombre de feuilles: "+str(document.nsheets))
print("Noms des feuilles: "+str(document.sheet_names()))