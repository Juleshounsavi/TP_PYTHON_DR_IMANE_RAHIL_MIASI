
import re

contenu_brut = """
   Ceci est une ligne valide.    
    Ligne avec des espaces superflus au debut.
Une ligne propre.
    
###@Ligne contenant des caractères non valides###!
Une autre ligne propre.  

   
"""

with open("texte_brut.txt", "w") as fichier:
    fichier.write(contenu_brut)


with open("texte_brut.txt", "r") as fichier:
    lignes = fichier.readlines()

lignes_nettoyees = []
for ligne in lignes:
    ligne = ligne.strip()  
    if not ligne:  
        continue
    ligne = re.sub(r"[^a-zA-Z0-9 .,!?-]", "", ligne)
    lignes_nettoyees.append(ligne)

with open("texte_nettoye.txt", "w") as fichier:
    fichier.write("\n".join(lignes_nettoyees))

with open("texte_nettoye.txt", "r") as fic:
    cont = fic.read()
    print(cont)





















