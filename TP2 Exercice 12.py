
age = int(input("Entrez l'age de la personne:"))
if age > 0 and age < 18:
    print("la personne est mineur.")
elif age >= 18:  
    print("la personne est majeur.")
else:
    print("Saisie incorrecte.")