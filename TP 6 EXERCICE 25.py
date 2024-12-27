
def comparer_fichiers(fichier1, fichier2):
    with open(fichier1, 'r') as file1, open(fichier2, 'r') as file2:
        lignes_fichier1 = file1.readlines()
        lignes_fichier2 = file2.readlines()

    differences = []    
    for i, (ligne1, ligne2) in enumerate(zip(lignes_fichier1, lignes_fichier2)):
        if ligne1 != ligne2:
            differences.append(f"Ligne {i+1} :\nFichier 1 : {ligne1.strip()}\nFichier 2 : {ligne2.strip()}\n")
    
    if differences:
        print("\n".join(differences))
    else:
        print("Les fichiers sont identiques.")

comparer_fichiers('fichier1.txt', 'fichier2.txt')
