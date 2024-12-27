import os

rep = input("Entrez le nom du fichier: ")

if os.path.exists(rep):
    print("Le fichier existe.")
else:
    print("Le fichier n'existe pas.")
