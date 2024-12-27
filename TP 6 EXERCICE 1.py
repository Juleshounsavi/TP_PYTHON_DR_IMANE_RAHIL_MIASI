
phrase = "Exemple de phrase\nExemple de phrase\nExemple de phrase."
with open("fichier.txt","w") as fichier:
    fichier.write(phrase)
    
with open("fichier.txt","r") as fichier:    
    fic = fichier.read()
    print(fic)

