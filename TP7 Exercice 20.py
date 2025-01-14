
class Livre:
    def __init__(self, titre, auteur, annee_publication, isbn):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication
        self.isbn = isbn
        self.disponible = True

    def __str__(self):
        return f"{self.titre} par {self.auteur} ({self.annee_publication}) - ISBN: {self.isbn}"

    def emprunter(self):
        if self.disponible:
            self.disponible = False
            return True
        return False

    def retourner(self):
        self.disponible = True

class Membre:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.livres_empruntes = []

    def emprunter_livre(self, livre):
        if livre.emprunter():
            self.livres_empruntes.append(livre)
            print(f"{self.nom} a emprunté le livre: {livre.titre}")
        else:
            print(f"{livre.titre} n'est pas disponible pour l'emprunt.")

    def retourner_livre(self, livre):
        if livre in self.livres_empruntes:
            livre.retourner()
            self.livres_empruntes.remove(livre)
            print(f"{self.nom} a retourné le livre: {livre.titre}")
        else:
            print(f"{self.nom} n'a pas emprunté ce livre.")

class Bibliotheque:
    def __init__(self):
        self.livres = []
        self.membres = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def ajouter_membre(self, membre):
        self.membres.append(membre)

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre disponible dans la bibliothèque.")
        for livre in self.livres:
            dispo = "Disponible" if livre.disponible else "Non disponible"
            print(f"{livre} - {dispo}")

    def rechercher_livre(self, titre):
        for livre in self.livres:
            if titre.lower() in livre.titre.lower():
                print(livre)

# Exemple d'utilisation
bibliotheque = Bibliotheque()

# Ajouter des livres
livre1 = Livre("1984", "George Orwell", 1949, "1234567890")
livre2 = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 1943, "0987654321")
bibliotheque.ajouter_livre(livre1)
bibliotheque.ajouter_livre(livre2)

# Ajouter des membres
membre1 = Membre("Alice", 1)
membre2 = Membre("Bob", 2)
bibliotheque.ajouter_membre(membre1)
bibliotheque.ajouter_membre(membre2)

# Afficher les livres disponibles
bibliotheque.afficher_livres()

# Alice emprunte un livre
membre1.emprunter_livre(livre1)

# Afficher les livres après emprunt
bibliotheque.afficher_livres()

# Bob essaie d'emprunter un livre non disponible
membre2.emprunter_livre(livre1)

# Alice retourne son livre
membre1.retourner_livre(livre1)

# Afficher les livres après retour
bibliotheque.afficher_livres()

# Rechercher un livre
bibliotheque.rechercher_livre("1984")
