import plateau
import vehicule

P1 = plateau.Plateau()
print(P1)

V1 = vehicule.vehicule(3, "H", 1, 2)
print(V1.afficher())
print(V1.cases())
V1.deplacer("droite")
print(V1.afficher())
print(V1.cases())
