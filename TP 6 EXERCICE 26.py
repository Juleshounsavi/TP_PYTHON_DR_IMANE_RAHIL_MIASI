
def compteur(fichier, mot):
    with open(fichier, 'r') as fic:
        contenu = fic.read()
    return contenu.lower().split().count(mot.lower())

mot = str(input("Entrez un mot à rechercher dans le fichier: "))
nom_fichier = str(input("Entrez le nom du fichier: "))  

occurences = compteur(nom_fichier, mot)
print("Le mot {} apparaît {} fois dans le fichier.".format(mot,occurences))
