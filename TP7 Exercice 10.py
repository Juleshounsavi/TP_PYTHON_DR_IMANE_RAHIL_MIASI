
class Employe:
    def __init__(self, nom, age, salaire):
        self.nom = nom
        self.age = age
        self.__salaire = salaire  # Le double underscore __ montre que c'est un attribut privé
    
    def mettre_a_jour_salaire(self, nouveau_salaire):
        if nouveau_salaire > 0:
            self.__salaire = nouveau_salaire
        else:
            print("Erreur : Le salaire doit être un montant positif.")
    
    def obtenir_salaire(self):
        return self.__salaire