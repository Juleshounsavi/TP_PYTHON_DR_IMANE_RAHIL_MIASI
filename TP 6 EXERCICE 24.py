
import csv

data = [
    {'Nom': 'A', 'Âge': 25, 'Ville': 'Marrakech'},
    {'Nom': 'B', 'Âge': 30, 'Ville': 'Casablanca'},
    {'Nom': 'C', 'Âge': 35, 'Ville': 'Rabat'}
]

with open('tableau.csv', "w") as fic:
    writer = csv.DictWriter(fic, fieldnames=['Nom', 'Âge', 'Ville'])
    writer.writeheader()
    writer.writerows(data)

with open("tableau.csv", "r") as fic:
    cont = fic.read()
    print(cont)