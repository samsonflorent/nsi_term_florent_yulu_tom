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
        self.voitures= []
    def __str__(self):
        for ligne in self.plateau:
            return(" ".join(ligne))
    def addCar(self, voiture):
        self.voitures.append(voiture)
