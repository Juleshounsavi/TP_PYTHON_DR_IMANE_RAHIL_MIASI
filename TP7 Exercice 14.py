
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.set_age(age)  

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError("L'âge doit être un entier.")
        if age < 0:
            raise ValueError("L'âge doit être un entier positif.")
        self.age = age

    
