
class Personne():
    def __init__(self,nom):
        self.nom = nom
        
p1 = Personne("Omar1")
p2 = Personne("Omar2")
p3 = Personne("Omar3")

noms = [p1.nom, p2.nom, p3.nom]
for nom in noms:
    print("Nom: {}".format(nom))