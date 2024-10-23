
notes = [12,10,13,4,5,6,7,8,19,15,11,12,18,14,20]

inf_7 = []
entre_7_et_10 = []
sup_10 = []

for note in notes:
    if note < 7:
        inf_7.append(note)
    elif note >= 7 and note < 10:
        entre_7_et_10.append(note)
    elif note >= 10 and note <= 20:
        sup_10.append(note)
        
print("Nombres d'etudiants ayant obtenue une note inferieur à 7:", len(inf_7))
print("Nombres d'etudiants ayant obtenue une note comprise entre 7 et 10:", len(entre_7_et_10))         
print("Nombres d'etudiants ayant obtenue une note superieur à 10:", len(sup_10))         
   

print("Note minimale:", min(notes)) 
print("Note maximale:", max(notes))  
print("Moyenne:", sum(notes)/len(notes))   
         
