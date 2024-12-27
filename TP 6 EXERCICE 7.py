
liste1 = [i for i in range(1,101)]
liste2 = "\n".join(map(str, liste1))

with open("fic7.txt","w") as fic:
    fic.write(liste2)
    
with open("fic7.txt","r") as fichier:    
    fic = fichier.read()
    print(fic)