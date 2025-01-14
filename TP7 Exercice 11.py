
class Employe:
    def __init__(self, nom, age, salaire):
        self.nom = nom
        self.age = age
        self.__salaire = salaire

    @property
    def voir_salaire(self):
        return self.__salaire

    @salaire.setter
    def changer_salaire(self, nouveau_salaire):
        if nouveau_salaire > 0:
            self.__salaire = nouveau_salaire
        else:
            raise ValueError("Le salaire doit être un montant positif.")

    