
class Etudiant:
    def __init__(self, nom):
        self.nom = nom
        
        
class Employe:
    def __init__(self, code):
        self.code = code
    
    
class EtudiantEmploye(Etudiant, Employe):
    def __init__(self, nom, code, salaire):
        Etudiant.__init__(self, nom)  #Alternative: super().__init__(nom)         
        Employe.__init__(self, code) #Alternative: super().__init__(code)
        self.salaire = salaire