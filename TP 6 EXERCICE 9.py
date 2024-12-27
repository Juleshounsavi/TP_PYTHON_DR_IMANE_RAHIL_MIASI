
liste = [
    "Le ciel est bleu.",
    "La terre est ronde.",
    "Le chat est sur le canapé.",
    "Python est un langage de programmation.",
    "L'arbre est dans le jardin."]

with open("fic9.txt", "w") as fic:
    for li in liste:
        fic.write(li + "\n")

mot = input("Entrez le mot à rechercher pour supprimer les lignes correspondantes: ")

with open("fic9.txt", "r") as file:
    lignes = file.readlines()

filtre = [ligne for ligne in lignes if mot not in ligne]

with open("fic9.txt", "w") as fic:
    fic.writelines(filtre)

print("Voici les lignes restantes après suppression:")
for ligne in filtre:
    print(ligne)
