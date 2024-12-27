
import csv
donnees = [
    ["Nom", "Âge", "Ville"],
    ["Alice", 30, "Paris"],
    ["Bob", 25, "Lyon"],
    ["Charlie", 35, "Marseille"]]

with open("fic11.csv", "w") as fic:
    writer = csv.writer(fic)
    writer.writerows(donnees)

with open("personnes.csv","r") as fic:
    lecteur = csv.DictReader(fic)
    for ligne in lecteur:
        print(dict(ligne))  