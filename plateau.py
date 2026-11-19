from vehicule import Vehicule
from colorama import Fore, Style, init

init(autoreset=True)


class Plateau:
    def __init__(self):
        self.plateau = [
            [". " for _ in range(6)]
            for _ in range(6)
        ]

        self.voitures = []
        self.porte = (2, 5)
        self.state = "p"

        # Choix du niveau
        while True:
            try:
                numero = int(input("Choisissez un niveau : "))

                if 1 <= numero <= 99:
                    self.numero_niveau = numero
                    break
                else:
                    print("Veuillez choisir un niveau entre 1 et 99.")

            except ValueError:
                print("Veuillez entrer un nombre valide.")
        self.charger_niveau(self.numero_niveau)
        
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

    # Vérifier que la direction correspond à l'orientation
    if voiture.orientation == "H" and direction not in ["gauche", "droite"]:
        print("Cette voiture est horizontale !")
        return

    if voiture.orientation == "V" and direction not in ["haut", "bas"]:
        print("Cette voiture est verticale !")
        return

    # Calculer les nouvelles positions sans déplacer immédiatement
    dx = 0
    dy = 0

    if direction == "haut":
        dx = -1
    elif direction == "bas":
        dx = 1
    elif direction == "gauche":
        dy = -1
    elif direction == "droite":
        dy = 1
    else:
        print("Direction invalide.")
        return

    nouvelles_cases = [
        (x + dx, y + dy)
        for x, y in voiture.cases()
    ]

    anciennes_cases = set(voiture.cases())

    # Vérifier les obstacles et les limites
    for x, y in nouvelles_cases:

        if not (0 <= x < 6 and 0 <= y < 6):
            print("Déplacement impossible : limite du plateau.")
            return

        if self.plateau[x][y] != ". " and (x, y) not in anciennes_cases:
            print("Déplacement impossible : voiture bloquée.")
            return

    # Effectuer le déplacement
    voiture.x += dx
    voiture.y += dy

    # Actualiser le plateau
    self.actualiser_plateau()

    print("Déplacement effectué !")


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
