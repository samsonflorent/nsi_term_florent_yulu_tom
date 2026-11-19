from vehicule import Vehicule
from colorama import Fore, Style, init

init(autoreset=True)


class Plateau:
    def __init__(self, plateau):
        self.plateau = plateau
        self.convertir_en_voitures()
        self.voitures = []
        self.porte = (2, 6)
        self.state = "p"
        
    def __str__(self):
        nuancier = {
            "R": Fore.RED,             # Rouge
            "B": Fore.BLUE,            # Bleu
            "V": Fore.GREEN,           # Vert
            "J": Fore.YELLOW,          # Jaune
            "M": Fore.MAGENTA,         # Magenta
            "C": Fore.CYAN,            # Cyan
            "G": Fore.LIGHTBLACK_EX,   # Gris
            "O": Fore.LIGHTRED_EX,     # Orange (approximatif)
            "P": Fore.LIGHTMAGENTA_EX, # Rose
            "L": Fore.LIGHTBLUE_EX,    # Bleu clair
            "T": Fore.LIGHTGREEN_EX,   # Vert clair
            "W": Fore.WHITE            # Blanc
        }
        affichage = ""
        for ligne in self.plateau:
            ligne_coloree = []
            for element in ligne:
                case = str(element)
                # Si la case fait 2 caractères et que la première lettre est une couleur connue
                if len(case) == 3 and case[0] in nuancier:
                    couleur = nuancier[case[0]]
                    symbole = case[1]
                    str_element = f"{couleur}{symbole}{Style.RESET_ALL} "
                else:
                    str_element = element
                ligne_coloree.append(str_element)
            affichage += " ".join(ligne_coloree) + "\n"
        return affichage

    def ajtvoiture(self, voiture):
        self.voitures.append(voiture)
        self.actualiser_plateau()

    def suppvoiture(self, voiture):
        if voiture in self.voitures:
            self.voitures.remove(voiture)
            self.actualiser_plateau()

    def position(self, voiture):
        return (voiture.x, voiture.y)

    def mouvementdevoiture(self, voiture, direction):
        x, y = self.position(voiture)
        if direction == "haut":
             if y > 0 and self.plateau[x][y+1] == ". ":
                self.plateau[x][y] = ". "
                self.plateau[x][y+1]=voiture       
        if direction == "bas":
            if y > 0 and self.plateau[x][y-1] == ". ":
                self.plateau[x][y] = ". "
                self.plateau[x][y-1]=voiture    
        if direction == "gauche":
            if x > 0 and self.plateau[x-1][y] == ". ":
                self.plateau[x][y] = ". "
                self.plateau[x-1][y]=voiture    
        if direction == "droite":
            if x+1 < 6 and self.plateau[x+1][y] == ". ":
                self.plateau[x][y] = ". "
                self.plateau[x+1][y]=voiture

    def getState(self):
        return self.state
    def sortie(self,voiture):
        x,y = self. position(voiture)
        if (x,y) == self.porte:
            self.suppvoiture(voiture)
            print("bien joué vous avez passé le niveau !")
            self.state = "w"
    def actualiser_plateau(self):
        """Reconstruit le plateau à partir des voitures."""

        # On vide le plateau
        self.plateau = [
            [". " for _ in range(6)]
            for _ in range(6)
        ]

        # On replace toutes les voitures
        for voiture in self.voitures:
            for x, y in voiture.cases():

                if 0 <= x < 6 and 0 <= y < 6:
                    self.plateau[x][y] = voiture
    def convertir_en_voitures(self):
        self.voitures = []
        voitures_trouvees = {}
    
        for x in range(6):
            for y in range(6):
                case = self.plateau[x][y]
    
                if case != ". ":
                    couleur = case[:2]
    
                    if couleur not in voitures_trouvees:
                        voitures_trouvees[couleur] = []
    
                    voitures_trouvees[couleur].append((x, y))
    
        for couleur, positions in voitures_trouvees.items():
        
            # On détermine l'orientation
            if len(positions) == 1:
                orientation = "H"  # À adapter si une voiture de taille 1 existe
            elif all(p[0] == positions[0][0] for p in positions):
                orientation = "H"
            else:
                orientation = "V"
    
            x = min(p[0] for p in positions)
            y = min(p[1] for p in positions)
    
            voiture = Vehicule(
                len(positions),
                orientation,
                x,
                y,
                couleur
            )
    
            self.voitures.append(voiture)
            