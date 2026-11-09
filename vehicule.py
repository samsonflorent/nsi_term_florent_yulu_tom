class Vehicule:

    def __init__(self,taille,orientation,x,y):
        self.taille=taille
        self.orientation=orientation
        self.x=x
        self.y=y

    def cases(self):
        resultat = []
        for i in range(self.taille):
            if self.orientation == "H":
                resultat.append((self.x, self.y + i))
            else:
                resultat.append((self.x + i, self.y))
        return resultat

    def afficher(self):
        return f"Vehicule({self.taille}, {self.orientation}, {self.x}, {self.y})"
