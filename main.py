import plateau
import vehicule

def display_menu():
    print("""
╔══════════════════════════════════════╗
║                                      ║
║             RUSH HOUR                ║
║                                      ║
╠══════════════════════════════════════╣
║                                      ║
║          1. Jouer                    ║
║          2. Choisir un niveau        ║
║          3. Instructions             ║                
║          4. Quitter                  ║
║                                      ║
╚══════════════════════════════════════╝
""")

def display_game(p):
    print(p)

def main():
    while True:
        display_menu()
        choice = input("Votre choix : ")

        if choice == "1":
            charger_niveau(1)
            display_game()
            input("Appuyez sur Entrée pour revenir...")
        elif choice == "2":
            print("Sélection du niveau")
            n = int(input("Quel niveau voulez-vous : "))
            p = charger_niveau(n)
            if p is not None:
                display_game(p)
        elif choice == "3":
            print("Déplacez les véhicules pour libérer X.")
        elif choice == "4":
            print("Au revoir !")
        else:
            print("Choix invalide.")



def charger_niveau(numero):
    try:
        module = __import__(
            f"cartes.niveau_{numero:02d}",
            fromlist=["plateau"]
        )

        donnees_plateau = module.plateau
        p = plateau.Plateau(donnees_plateau)

        return p

    except ModuleNotFoundError:
        print("Ce niveau n'existe pas.")
        return None


if __name__ == "__main__":
    main()
