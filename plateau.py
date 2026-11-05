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
        self.position_car=(x, y)
    def __str__(self):
        for ligne in self.plateau:
            return(" ".join(ligne))
    def addCar(self, voiture):
        self.voitures.append(voiture)
    def removeCar(self, voiture):
        self.voitures.remove(voiture)
    def position(self, voiture):
        for x in range(len(self.plateau)):
            for y in range(len(self.plateau[x])):
                if self.plateau[x][y] == voiture:
                    return (x, y)
        return None
    def mouvementdecar(self, voiture, direction):
        
    

