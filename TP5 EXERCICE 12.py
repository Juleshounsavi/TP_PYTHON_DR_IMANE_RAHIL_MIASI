
def compte_occurrences(liste, element):
    compteur = 0
    for i in liste:
        if i == element:
            compteur = compteur + 1
    return compteur
