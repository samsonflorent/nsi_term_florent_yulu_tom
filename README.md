# nsi_term_florent_yulu_tom
class Plateau:
    def __init__(self):
        self.plateau = [
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "]
        ]
    def __str__(self):
        for ligne in self.plateau:
            return(" ".join(ligne))
    def addCar(self):
        self.moncar=self.voiture

class Vehicule:
    def __init__(self, nom, taille, orientation, x, y):
        self.nom = nom
        self.taille = taille
        self.orientation = orientation
        self.x = x
        self.y = y
