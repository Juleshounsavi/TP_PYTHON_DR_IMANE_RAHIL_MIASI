
contenu_initial = [
    "Ligne 1 : Ceci est la premiere ligne.",
    "Ligne 2 : Ceci est la deuxieme ligne.",
    "Ligne 3 : Ceci est la troisieme ligne.",
    "Ligne 4 : Ceci est la quatrieme ligne."
]

with open("fic17.txt", "w") as fic:
    for ligne in contenu_initial:
        fic.write(ligne + "\n")


try:
    print("\nContenu initial du fichier:\n")
    with open(nom_fichier, "r") as fic:
        lignes = fic.readlines()
        for ligne in lignes:
            print(ligne)
    ligne_a_modifier = int(input("\nEntrez le numéro de la ligne à modifier : "))
    if ligne_a_modifier < 1 or ligne_a_modifier > len(lignes):
        print("Numéro de ligne invalide.")
    else:
        nv_cont = input("Entrez le nouveau contenu pour cette ligne : ")
        lignes[ligne_a_modifier - 1] = nv_cont + "\n"
        with open(nom_fichier, "w", encoding="utf-8") as fichier:
            fichier.writelines(lignes)
        print("\nNouveau contenu du fichier:")
        for ligne in lignes:
            print(ligne)

except FileNotFoundError:
    print("Le fichier fic17.txt n'existe pas.")
except ValueError:
    print("Veuillez entrer un numéro de ligne valide.")
except Exception as e:
    print("Une erreur s'est produite: e.")
