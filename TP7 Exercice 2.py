
class Personne():
    def __init__(self,nom):
        self.nom = nom
        
    def saluer(self):
        return "Bienvenue " + str(self.nom) + "."

p = Personne("Omar")
print(p.saluer())