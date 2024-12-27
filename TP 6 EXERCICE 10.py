
import os

ancien = str(input("Entrez le nom du fichier à renommer: "))
nouveau = str(input("Entrez le nouveau nom du fichier à renommer: "))

if os.path.exists(ancien):
    os.rename(ancien, nouveau)
else:
    print("Erreur : Le fichier '{}' n'existe pas.".format(ancien))
