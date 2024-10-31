
ma_liste = [15,25,35,45,55]
print("Dernier élement:", ma_liste[-1])
ma_liste[2] = 40
print("Liste modifié:", ma_liste)

ma_liste.append(65)
print("Liste modifié:", ma_liste)
ma_liste.append(75)
print("Liste modifié:", ma_liste)
ma_liste.insert(1,20)
print("Liste modifié:", ma_liste)

somme = 0
for i in ma_liste:
    somme = somme  + i
print("La somme de tous les élements de la liste:", somme)