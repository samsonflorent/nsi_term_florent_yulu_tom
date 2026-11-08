import vehicule

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
        self.porte = (2, 5)
    def __str__(self):
        affichage = ""
        for ligne in self.plateau:
            affichage += " ".join(ligne) + "\n"
        return affichage
    def addCar(self):
        self.voitures.append(voiture)
    def removeCar(self, voiture):
        self.voitures.remove(voiture)
    def position(self, voiture):
        for x in range(len(self.plateau)):
            for y in range(len(self.plateau[x])):
                if self.plateau[x][y] == voiture:
                    return (x, y)
        return None
#    def mouvementdecar(self, voiture, direction):