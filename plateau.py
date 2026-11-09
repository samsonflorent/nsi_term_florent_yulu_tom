#import vehicule
from colorama import Fore, Style, init

init(autoreset=True)
class Plateau:
    def __init__(self):
        self.plateau = [
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", "BV ", ". ", ". ", ". ", ". "],
            [". ", "GV ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", "VV ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "],
            [". ", ". ", ". ", ". ", ". ", ". "]
        ]
        self.voitures= []
        self.porte = (2, 5)
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
