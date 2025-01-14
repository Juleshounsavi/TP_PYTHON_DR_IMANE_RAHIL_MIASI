
class Personne:
    population_totale = 0  
    
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
        Personne.population_totale += 1  
        
    def __del__(self):
        Personne.population_totale -= 1

    @classmethod
    def afficher_population_totale(cls):
        return f"Population totale : {cls.population_totale}"