
nom = str(input("Entrez le nom:")) 
prenom = str(input("Entrez le prenom:"))
age = int(input("Entrez l'âge:"))
if age <= 0:
    print("Saisie incorrecte.")
elif age == 1:
    print("La personne s'appelle " + nom + " " + prenom + " et est agée de " + str(age) + " an.")
elif age > 1:
    print("La personne s'appelle " + nom + " " + prenom + " et est agée de " + str(age) + " ans.")    

