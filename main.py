from Etat import Etat, Cout
from Ida import Ida
import copy

game = Etat(3, 3, Cout.NON_UNIFORME)

#deepcopy copie tout les objects (pas de pointeur partagés)
ida = Ida(copy.deepcopy(game))

game.afficher_etat()
game.trouver_destinations(1)
game = game.deplacer(0, 3)
game.afficher_etat()
game.trouver_destinations(2)
game = game.deplacer(0, 3)
game.afficher_etat()

#test si game est but de ida
print(ida.estBut(game))

list = game.opPoss()
for i in range(len(list)):
	print(list[i])
