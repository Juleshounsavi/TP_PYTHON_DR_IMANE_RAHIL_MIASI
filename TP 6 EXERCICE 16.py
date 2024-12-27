
import csv

donnees = [
    {"col1": "A1", "col2": "B1", "col3": "C1"},
    {"col1": "A2", "col2": "B2", "col3": "C2"},
    {"col1": "A3", "col2": "B3", "col3": "C3"},
]

with open("fic16.csv", "w") as fic:
    writer = csv.DictWriter(fic, fieldnames=["col1", "col2", "col3"])
    writer.writeheader()
    writer.writerows(donnees)

colonne = input("Entrez le nom de la colonne à extraire (col1, col2, col3): ")

try:
    with open("fic16.csv", "r") as fic:
        reader = csv.DictReader(fic)
        if colonne not in reader.fieldnames:
            print("La colonne {} n'existe pas.".format(colonne))
        else:
            print("Contenu de la colonne {}: ".format(colonne))
            for ligne in reader:
                print(ligne[colonne])
except FileNotFoundError:
    print("Le fichier fic16.csv n'existe pas.")
except Exception as e:
    print("Une erreur s'est produite : e")
