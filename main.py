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

def play_game(p):
    s = True
    while s == True:
        print(f"\n{p}")
        userCarChoiceInput = input("Quelle vehicule voulez vous sélectionner (v : voiture, c : camion) : ").lower()
        if userCarChoiceInput not in ["v", "c"]:
            print("Type de véhicule invalide.")
            continue
        userColorChoiceInput = input("De quelle couleur est votre vehicule (Rouge : R, Bleu : B, Jaune : J, Orange : O, ... et ainsi de suite, ? : liste des caractères/couleurs ) : ").upper()
        if userColorChoiceInput == "?":
            print("R -> Rouge \nB->Bleu \nV->Vert \nJ->Jaune \nM->Magenta \nC->Cyan \nG->Gris \nO->Orange \nP->Rose")
            continue
        vehicule_selectionne = None

        for voiture in p.voitures:

            # On vérifie la couleur
            if voiture.couleur[0] != userColorChoiceInput:
                continue

            # On vérifie le type
            if userCarChoiceInput == "v" and voiture.taille == 2:
                vehicule_selectionne = voiture
                break

            elif userCarChoiceInput == "c" and voiture.taille == 3:
                vehicule_selectionne = voiture
                break

        if vehicule_selectionne is None:
            print("Aucun véhicule correspondant trouvé.")
            continue

        print(vehicule_selectionne.afficher())

        direction = input(
            "Dans quelle direction voulez-vous le déplacer "
            "(haut:H, bas:B, gauche:G, droite:D) ? "
        ).upper()
        
        directions = ["D","G","H","B"]
        
        if direction not in directions:
            print("Direction invalide.")
            continue

        if p.mouvementdevoiture(vehicule_selectionne,direction):
            print("Déplacement réussi !")
        else:
            print("Déplacement impossible !")

def main():
    while True:
        display_menu()
        choice = input("Votre choix : ")
        if choice == "1":
            p = charger_niveau(1)
            if p is not None:
                play_game(p)
                input("Appuyez sur Entrée pour revenir...")
        elif choice == "2":
            print("Sélection du niveau")
            vtemp = False
            while not(vtemp):
                n = (input("Quel niveau voulez-vous : "))
                if n.isdigit():
                    if 0<int(n) and int(n)<=40:
                        vtemp = True
                        continue
                print("Utilise un entier stp entre 1 et 40")
            p = charger_niveau(int(n))
            if p is not None:
                play_game(p)
        elif choice == "3":
            print("Déplacez les véhicules pour libérer X.")
        elif choice == "4":
            print("Au revoir !")
            break
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
