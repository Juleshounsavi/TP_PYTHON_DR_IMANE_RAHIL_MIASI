
class Personne:
    def __init__(self, nom, age):
        self.age = age
        if not self.nom_valide(nom):
            raise ValueError("Le nom doit être une chaîne non vide.")
        self.nom = nom

    @staticmethod
    def nom_valide(nom):
        return isinstance(nom, str) and len(nom.strip()) > 0

    