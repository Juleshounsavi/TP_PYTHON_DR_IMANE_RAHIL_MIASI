
etudiants = {
    "Alice":16,
    "Bob":12,
    "Charlie":8,
    "David":14,
    "Emma":10,
    "Fiona":18,
    "George":7,
    "Hannah":15,
    "Ivan":13,
    "Jane":9,
    }
print(etudiants.items())
print("-"*50)

moy = (sum(etudiants.values()))/(len(etudiants.values()))
note_max = max(etudiants.values())
note_min = min(etudiants.values())
etudiant_max = [eleve for eleve, note in etudiants.items() if note == note_max]
etudiant_min = [eleve for eleve, note in etudiants.items() if note == note_min]
print("Note maximale: {}\nEtudiant:{} .".format(note_max,etudiant_max))
print("-"*50)
print("Note minimale: {}\nEtudiant:{} .".format(note_min,etudiant_min))

Admis = []
Rattrapage = []
Ajourne = []

for etudiant, note in etudiants.items():
    if note >= 10:
        Admis.append(etudiant)
    elif 5 <= note <= 9:
        Rattrapage.append(etudiant)
    elif note <5:
        Ajourne.append(etudiant)
        
print("Etudiants admis:", Admis)
print("-"*50)
print("Etudiants en rattrapage:", Rattrapage)
print("-"*50)
print("Etudiants ajournés:", Ajourne)
print("-"*50)

nom = str(input("Entrez le nom de l'étudiant:")) 
if nom in etudiants.keys():
    print("Note:", etudiants[nom])
else:
    print("Saisie incorrecte.")      
print("-"*50)
    
rep1 = str(input("Voulez-vous mettre à jour une note? (repondez par oui ou non)"))   
if rep1 == "oui":
    nom1 = str(input("Entrez le nom de l'étudiant:"))
    note1 = float(input("Entrez la note de l'étudiant:"))
etudiants[nom1] = note1
print("Dictionnaire modifié:", etudiants.items())
print("-"*50)

rep2 = str(input("Voulez-vous ajouter une note? (repondez par oui ou non)"))   
if rep2 == "oui":
    nom2 = str(input("Entrez le nom de l'étudiant:"))
    note2 = float(input("Entrez la note de l'étudiant:"))
etudiants[nom2] = note2
print("Dictionnaire final:", etudiants.items())
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        