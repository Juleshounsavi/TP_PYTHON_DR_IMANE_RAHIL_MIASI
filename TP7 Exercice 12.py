
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def travail(self):
        return f"{self.nom} est occupé à quelque chose d'indéfini."


class Employe(Personne):
    def __init__(self, nom, age, profession):
        super().__init__(nom, age) #Appel les attributs de la classe Pere
        self.profession = profession
    def travail(self):
        return f"{self.nom} travaille en tant que {self.profession}."


class Etudiant(Personne):
    def __init__(self, nom, age, domaine):
        super().__init__(nom, age)
        self.domaine = domaine
    def travail(self):
        return f"{self.nom} étudie dans le domaine de {self.domaine}."

