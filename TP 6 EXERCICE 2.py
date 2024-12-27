
texte = str(input("Veuillez entrez un texte:"))
with open("output.txt","w") as output:
    output.write(texte)

print("Affichage du texte:")
with open("output.txt","r") as output:    
    fic = output.read()
    print(fic)
    
