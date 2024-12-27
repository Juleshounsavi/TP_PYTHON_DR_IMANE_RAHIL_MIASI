
import os
import shutil
from datetime import datetime

if not os.path.exists("original.txt"):
    with open("original.txt", "w") as fichier:
        fichier.write("Ceci est le contenu du fichier original.")

if not os.path.exists("backup"):
    os.makedirs("backup")

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

nom_fichier = os.path.basename("original.txt")  
nom_sauvegarde = f"{os.path.splitext(nom_fichier)[0]}_{timestamp}{os.path.splitext(nom_fichier)[1]}"
chemin_sauvegarde = os.path.join("backup", nom_sauvegarde)

shutil.copy("original.txt", chemin_sauvegarde)

print(f"Le fichier original.txt a été sauvegardé sous '{chemin_sauvegarde}'.")
