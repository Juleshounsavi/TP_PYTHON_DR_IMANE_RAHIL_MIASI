
reponse = str(input("La personne fume t-elle?(Repondez par oui ou non)"))
age = int(input("Saisissez l'âge de la personne:"))
reponses = ["oui", "non"]

if age > 0 and reponse in reponses:
    if age > 60 and reponse == "oui":
        print("Le patient est une personne agee qui fume")
    elif age < 15 and reponse == "oui":
        print("C'est un enfant fumeur")
    elif (age>=15 and age<=60) and (reponse=="oui"):
            print("C'est un adulte fumeur")
    else:
        print("le patient ne fume pas")        
else:
    print("Saisie incorrecte.")        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    