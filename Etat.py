from Pique import Pique
from Cube import Cube


class Etat:

	#initialisation
	def __init__(self, nb_piques, cubes_par_pique):
		jeu = []
		compte = cubes_par_pique

		for i in range(nb_piques):
			pique = Pique(cubes_par_pique)

			for j in range(cubes_par_pique):
				cube = Cube(compte - j)
				pique.ajouter(cube)

			jeu.append(pique)
			compte += cubes_par_pique
		pique = Pique(cubes_par_pique)
		jeu.append(pique)

		self.nb_piques = nb_piques
		self.cubes_par_pique = cubes_par_pique
		self.jeu = jeu
		self.cout = 0

	#affiche l'etat
	def afficher_etat(self):

		for i in range(self.jeu[0].nb_cubes_max):
			for j in range(len(self.jeu)):
				print('|', end='')
				if (self.jeu[j].nb_cubes == 0):
					print(" ", end='')
				else:
					#Inverser affichage
					indice = self.jeu[j].nb_cubes_max - i - 1
					#Vérifier que l'indice existe
					if (self.jeu[j].nb_cubes > indice):
						print(self.jeu[j].liste[indice].chiffre, end='')
					else:
						print(" ", end='')
				print('|', end='')
			print("")

	#retourne vrai si la pique pleine, faux sinon
	def pique_pleine(self, p):
		return p.is_full()

	#Trouve les destination possibles (piques) en partant de pi
	#Et retourne une liste
	def trouver_destinations(self, pi):
		piques_vides = []
		j_ = 0

		for i in range(len(self.jeu)):
			if (i != pi - 1):
				if (self.pique_pleine(self.jeu[i]) == False):
					piques_vides.append(i + 1)

		print("Vous pouvez déplacer un cube sur la/les pique(s) : ", end='')
		for j in range(len(piques_vides) - 1):
			print(piques_vides[j], ", ", end='')
			j_ = j + 1
		print(piques_vides[j_], ".")
		return piques_vides

	#Deplace un cube de p1 à p2
	#Et retourne l'Etat fils resultant
	def deplacer(self, p1_from, p2_to):
		etat_fils = self
		cube_a_deplacer = etat_fils.jeu[p1_from - 1].retirer()
		etat_fils.jeu[p2_to - 1].ajouter(cube_a_deplacer)
		etat_fils.cout_uniforme()
		return etat_fils

	# return ( operation, etatFils, cout )
	def opPoss(self):
		triplet_list = []
		for i in range(4):
			dest = self.trouver_destinations(i)
			for j in range(len(dest)):
				etatFils = self.deplacer(i, dest[j])
				triplet_list.append(((j, dest[j]), etatFils, 1))
		return triplet_list

	#fonctions de coup
	def cout_uniforme(self):
		self.cout += 1

	def cout_non_uniforme(self, cout):
		self.cout += cout
