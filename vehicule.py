class vehicule:

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

    def deplacer(self, direction):
        if self.orientation == "H":
            if direction == "droite":
                self.y += 1
            elif direction == "gauche":
                self.y -= 1

        elif self.orientation == "V":
            if direction == "haut":
                self.x -= 1
            elif direction == "bas":
                self.x += 1

    def afficher(self):
        return f"vehicule({self.taille}, {self.orientation}, {self.x}, {self.y})"
