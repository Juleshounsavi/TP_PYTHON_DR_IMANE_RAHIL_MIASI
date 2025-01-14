
class Adresse:
    def __init__(self, rue, ville, code_postal):
        self.rue = rue
        self.ville = ville
        self.code_postal = code_postal

    def __str__(self):
        return f"{self.rue}, {self.ville}, {self.code_postal}"


class Personne:
    def __init__(self, nom, age, adresse):
        self.nom = nom
        self.age = age
        self.adresse = adresse  
    def __str__(self):
        return f"Personne : {self.nom}, Âge : {self.age} ans, Adresse : {self.adresse}"
