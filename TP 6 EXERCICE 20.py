
import csv
import math

with open('notes.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['notes1', 'notes2', 'notes3'])
    writer.writerow([15, 12, 18])
    writer.writerow([13, 14, 17])
    writer.writerow([16, 13, 19])
    writer.writerow([14, 15, 16])

def calcul_stats(nom_fichier, colonne):
    valeurs = []
    with open(nom_fichier, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            valeurs.append(float(row[colonne]))
    somme = sum(valeurs)
    moyenne = somme / len(valeurs)
    ecart_type = math.sqrt(sum((x - moyenne) ** 2 for x in valeurs) / len(valeurs))
    return somme, moyenne, ecart_type

somme, moyenne, ecart_type = calcul_stats('notes.csv', 0)
print("Somme: {}\nMoyenne: {}\nEcart-type: {}".format(somme,moyenne,ecart_type))
