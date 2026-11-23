from vehicule import Vehicule
from colorama import Fore, Style, init

init(autoreset=True)


class Plateau:
    def __init__(self, plateau):
        self.plateau = plateau
        self.voitures = []
        self.convertir_en_voitures()
        self.porte = (2, 5)
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
                    str_element = case
                ligne_coloree.append(str_element)
            affichage += " ".join(ligne_coloree) + "\n"
        return affichage

    def ajtvoiture(self, voiture):                                 #ajouté une voiture
        self.voitures.append(voiture)
        self.actualiser_plateau()

    def suppvoiture(self, voiture):                                #supprimé la voiture
        if voiture in self.voitures:
            self.voitures.remove(voiture)
            self.actualiser_plateau()

    def position(self, voiture):                                    #get la position de la voiture
        return (voiture.x, voiture.y)

    
    def mouvementdevoiture(self, voiture, direction):

        # Vérifier que la direction correspond à l'orientation
        if voiture.orientation == "H" and direction not in ("D", "G"):
            return False
        if voiture.orientation == "V" and direction not in ("H", "B"):
            return False
        dx, dy = 0, 0
        if direction == "D":
            dy = 1
        elif direction == "G":
            dy = -1
        elif direction == "B":
            dx = 1
        elif direction == "H":
            dx = -1
        anciennes_cases = voiture.cases()
        nouvelles_cases = [
            (x + dx, y + dy)
            for x, y in anciennes_cases
        ]
        for x, y in nouvelles_cases:
            if not (0 <= x < 6 and 0 <= y < 6):
                return False
            if (x, y) not in anciennes_cases:
                if self.plateau[x][y] != ". ":
                    return False
        voiture.x += dx
        voiture.y += dy

        self.actualiser_plateau()
        return True

    def getState(self):
        return self.state
    def sortie(self,voiture):
        # c est la sortie pour la fin
        x,y = self. position(voiture)
        if (x,y) == self.porte:
            self.suppvoiture(voiture)
            print("bien joué vous avez passé le niveau !")
            self.state = "w"
    def actualiser_plateau(self):
        self.plateau = [
            [". " for _ in range(6)]
            for _ in range(6)
        ]

        for voiture in self.voitures:
            for x, y in voiture.cases():
                if 0 <= x < 6 and 0 <= y < 6:
                    self.plateau[x][y] = voiture.couleur + " "
    
    
    def convertir_en_voitures(self):
        self.voitures = []
        voitures_trouvees = {}

        for x in range(6):
            for y in range(6):
                case = str(self.plateau[x][y]).strip()

                if case and case != ".":
                    code = case[:2]

                    if code not in voitures_trouvees:
                        voitures_trouvees[code] = []

                    voitures_trouvees[code].append((x, y))

        for code, positions in voitures_trouvees.items():

            lignes = {pos[0] for pos in positions}
            colonnes = {pos[1] for pos in positions}

            if len(lignes) == 1:
                orientation = "H"
                x = positions[0][0]
                y = min(pos[1] for pos in positions)

            elif len(colonnes) == 1:
                orientation = "V"
                x = min(pos[0] for pos in positions)
                y = positions[0][1]

            else:
                raise ValueError(
                    f"Véhicule {code} mal placé : {positions}"
                )

            # La deuxième lettre détermine la catégorie
            if code[1] == "C":
                longueur = 3
            elif code[1] == "V":
                longueur = 2
            else:
                raise ValueError(f"Catégorie inconnue : {code}")

            if len(positions) != longueur:
                raise ValueError(
                    f"{code} devrait occuper {longueur} cases, "
                    f"mais en occupe {len(positions)}"
                )

            voiture = Vehicule(
                longueur,
                orientation,
                x,
                y,
                code
            )

            self.voitures.append(voiture)