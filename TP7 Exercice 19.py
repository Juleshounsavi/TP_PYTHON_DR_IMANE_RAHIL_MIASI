


class Personne:
    def __init__(self, nom, age):        
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Personne : {self.nom}, Âge : {self.age} ans."

    def __iter__(self):
        return iter(self.nom)

    def generer_premiere_lettre(self):
        print(self.nom[0])