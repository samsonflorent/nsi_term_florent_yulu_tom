import vehicule
from colorama import Fore, Style, init

init(autoreset=True)
class Plateau:
    def __init__(self):
        self.plateau = [
            [". ", ". ", ". ", ". ", ". ", "RC "],
            [". ", "BV ", "BV ", ". ", ". ", "RC "],
            [". ", "GV ", ". ", ". ", ". ", "RC "],
            [". ", "GV ", ". ", "VV ", ". ", ". "],
            [". ", ". ", ". ", "VV ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "]
        ]
        self.voitures= []
        self.porte = (2, 6)
        self.numero_niveau = 1
        self.charger_niveau(self.numero_niveau)
        #self.position_voiture(x,y)
    def __str__(self):
        nuancier = {
            "B": Fore.BLUE,
            "R": Fore.RED,
            "V": Fore.GREEN,
            "J": Fore.YELLOW,
            "M": Fore.MAGENTA,
            "C": Fore.CYAN,
            "G": Fore.LIGHTBLACK_EX  # Gris
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
    def charger_niveau(self, numero):
        module = __import__(f"niveau_{numero:02d}")
        self.plateau = module.plateau
    def ajtvoiture(self):
        self.voitures.append(voiture)
    def suppvoiture(self, voiture):
        self.voitures.remove(voiture)
    def position(self, voiture):
        for x in range(len(self.plateau)):
            for y in range(len(self.plateau[x])):
                if self.plateau[x][y] == voiture:
                    return (x, y)
        return None
#    def mouvementdecar(self, voiture, direction):
    def mouvementdevoiture(self, voiture, direction):
        x, y = self.position(voiture)
        if direction == " haut":
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
            if x > 0 and self.plateau[x+1][y] == ". ":
                self.plateau[x][y] = ". "
                self.plateau[x+1][y]=voiture
    def sortie(self,voiture):
        x,y = self. position(voiture)
        if (x,y) == self.porte:
            self.suppvoiture(voiture)
            print("bien joué vous avez passé le niveau !")
