from Etat import Etat

def estBut(e):
	return egal(e, but)


def egal(e, but):
	print(e.cubes_par_pique, e.nb_piques)
	for i in range(e.cubes_par_pique):
		for j in range(e.nb_piques):
			if (not e.jeu[j].liste[i].chiffre == but.jeu[j].liste[i].chiffre):
				return False
	return True


game = Etat(3, 3)

game.afficher_etat()

dest = game.trouver_destinations(1)

game.deplacer(1, 4)

game.afficher_etat()

game.trouver_destinations(2)

game.deplacer(1, 4)

game.afficher_etat()

print(egal(game, game))

print(game.opPoss()[0])
