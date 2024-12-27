
class Personne:
    population = 0
    def __init__(self, nom):
        self.nom = nom
        Personne.population += 1

    def __del__(self):
        Personne.population -= 1
