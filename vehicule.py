
class Vehicule:
    def __init__(self, taille, orientation, x, y):
        self.taille = taille
        self.orientation = orientation
        self.x = x
        self.y = y

    def cases(self):
        """Renvoie toutes les coordonnées occupées par la voiture."""
        resultat = []

        for i in range(self.taille):
            if self.orientation == "H":
                resultat.append((self.x, self.y + i))
            else:
                resultat.append((self.x + i, self.y))

        return resultat

    def deplacer(self, direction):
        """Déplace la voiture d'une case."""

        if self.orientation == "H":
            if direction == "D":
                self.y += 1
            elif direction == "G":
                self.y -= 1
            else:
                return False

        elif self.orientation == "V":
            if direction == "B":
                self.x += 1
            elif direction == "H":
                self.x -= 1
            else:
                return False

        return True

    def afficher(self):
        return f"Vehicule({self.taille}, {self.orientation}, {self.x}, {self.y})"
