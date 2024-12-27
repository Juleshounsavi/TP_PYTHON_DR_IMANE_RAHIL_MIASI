
texte = "ligne1\nligne2\nligne3"
with open("fic4.txt","w") as fic:
    fic.write(texte)
    
count = 0
with open("fic4.txt","r") as fichier:    
    lignes = fichier.readlines()
    for ligne in lignes:
        count = count + 1
    
print("Nombre de lignes: {}.".format(count))    