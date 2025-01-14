
class Personne:
    def __init__(self, nom, age, profession):
        self.nom = nom
        self.age = age
        self.profession = profession
    def obtenir_age(self):
        return self._age  # L'underscore _ montre que c'est un attribut protégé
    