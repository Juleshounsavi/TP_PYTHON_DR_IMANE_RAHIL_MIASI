
texte = "ligne1\nligne2\nligne3"
with open("fic5.txt","w") as fic:
    fic.write(texte)
    
    
with open("fic5.txt","r") as fichier:    
    lignes = fichier.readlines()
    for i, ligne in enumerate(lignes, start=1):
        print(str(i) + ":" + ligne)
