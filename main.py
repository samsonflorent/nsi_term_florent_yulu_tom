import plateau
import vehicule

P1 = plateau.Plateau()
print(P1)

V1 = vehicule.vehicule()
print(V1.afficher())
print(V1.cases())
V1.deplacer("")
print(V1.afficher())
print(V1.cases())
