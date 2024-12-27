
phrase = "\nAutre exemple de phrase\nAutre exemple de phrase\nAutre exemple de phrase."
with open("fichier.txt", "a") as fichier:
    fichier.write(phrase)
    
with open("fichier.txt","r") as fichier:    
    fic = fichier.read()
    print(fic)    
    
    
    