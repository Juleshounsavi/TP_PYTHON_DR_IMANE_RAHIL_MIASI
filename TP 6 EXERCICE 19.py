
import os

def lister_fichiers(repertoire):
    try:
        fichiers = [f for f in os.listdir(repertoire) if os.path.isfile(os.path.join(repertoire, f))]
        print(f"Fichiers dans le répertoire '{repertoire}':")
        for fichier in fichiers:
            print(fichier)
    except FileNotFoundError:
        print(f"Erreur : Le répertoire '{repertoire}' n'existe pas.")
    except Exception as e:
        print(f"Erreur : {e}")

repertoire = input("Entrez le chemin du répertoire: ")
lister_fichiers(repertoire)
