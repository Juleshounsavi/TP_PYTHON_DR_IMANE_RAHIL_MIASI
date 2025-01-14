
class Personne:
    def __init__(self, nom, age, profession):
        self.nom = nom
        self.age = age
        self.profession = profession
    
    def __str__(self):
        return "Personne : {}\nÂge : {} ans\nProfession : {}".format(self.nom, self.age, self.profession)

