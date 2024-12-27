
contenu1 = "Contenu du fichier input1"
with open("input1.txt","w") as fic:
    fic.write(contenu1)
    
with open("input1.txt","r") as input1, open("output1.txt","w") as output1:
    for ligne in input1:
        output1.write(ligne) 

with open("output1.txt", "r") as fichier:
    lignes = fichier.read()
    print(lignes)
    