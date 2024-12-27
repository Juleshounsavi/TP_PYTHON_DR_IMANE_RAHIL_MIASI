
fichiers = ["file1.txt", "file2.txt", "file3.txt"]
contenus = [
    "Ligne1 du fichier 1.\nLigne2 du fichier 1.\nLigne3 du fichier 1",
    "Ligne1 du fichier 2.\nLigne2 du fichier 2.\nLigne3 du fichier 2",
    "Ligne1 du fichier 3.\nLigne2 du fichier 3.\nLigne3 du fichier 3"
]

for i in range(len(fichiers)):
    with open(fichiers[i], "w") as fichier:
        fichier.write(contenus[i])

with open("merged.txt", "w") as merged:
    for fichier in fichiers:
        with open(fichier, "r") as f:
            contenu = f.read()
            merged.write(contenu + "\n\n")  
            
with open("merged.txt", "r") as fic:
    cont = fic.read()
    print(cont)            