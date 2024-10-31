
ages = [21,17,19,25,18,16,20,22,19]
moins = []
entre = []
plus = []

for age in ages:
    if age < 18:
        moins.append(age)
    elif age >= 18 and age <= 20:
        entre.append(age)
    elif age > 20:
        plus.append(age)

print("Les personnes ayant moins de 18 ans:", moins)    
print("Les personnes ayant entre 18 et 20 ans:", entre)        
print("Les personnes ayant plus de 20 ans:", plus)  

moy = (sum(ages))/(len(ages)) 
print("Age moyen des membres:", moy)         