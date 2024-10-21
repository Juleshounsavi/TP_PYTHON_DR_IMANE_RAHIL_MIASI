
poids = float(input("Entrez votre poids:"))
taille = float(input("Entrez votre taille:"))
if poids > 0 and taille > 0:
    imc = (poids)/(taille**2)   
    print("Votre IMC est:" + str(imc))   
else:
    print("Saisie incorrecte.")              
                   

