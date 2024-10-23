
ma_liste=[10,20,30,40,50]

print("Le premier element de la liste est:", ma_liste[0])
print("Le troisieme element de la liste est:", ma_liste[2])

reponse = 30 in ma_liste
if reponse == True:
    print("30 est dans la liste.")
else:
    print("30 n'est pas dans la liste.")
    
ma_liste[1] = 25
print(ma_liste)

print("Longueur de la liste:", len(ma_liste))

ma_liste.append(60)
print(ma_liste)
