from Pique import Pique
from Cube import Cube
from enum import Enum
import copy


class Cout(Enum):
	UNIFORME = 1
	NON_UNIFORME = 2


class Etat:

	#initialisation Etat
	def __init__(self, nb_piques, cubes_par_pique, type_cout):
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
		self.type_cout = type_cout  #class cout

	#get jeu
	def get_jeu(self):
		return self.jeu

	#get nb_piques
	def get_nb_piques(self):
		return self.nb_piques

	#get cubes_par_pique
	def get_cubes_par_pique(self):
		return self.cubes_par_pique

	#get cout
	def get_cout(self):
		return self.cout

	def get_pique(self, pi):
		return self.jeu[pi]

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
			if (i != pi):
				if (not self.pique_pleine(self.jeu[i])):
					piques_vides.append(i)

		print("Vous pouvez déplacer un cube sur la/les pique(s) : ", end='')
		for j in range(len(piques_vides) - 1):
			print(piques_vides[j], ", ", end='')
			j_ = j + 1
		print(piques_vides[j_], ".")
		return piques_vides

	#Deplace un cube de p1 à p2
	#Et retourne l'Etat fils resultant sans changer l'etat père
	def deplacer(self, p1_from, p2_to):

		#deepcopy copie tout les objects (pas de pointeur partagés)
		etat_fils = copy.deepcopy(self)
		cube_a_deplacer = etat_fils.jeu[p1_from].retirer()
		etat_fils.jeu[p2_to].ajouter(cube_a_deplacer)
		#etat_fils.increment_cout((p1_from, p2_to)) # A suprrimer car opPoss s'occupe d'incrementer
		return etat_fils

	# return ( operation, etatFils, cout )
	def opPoss(self):
		triplet_list = []
		for i in range(4):  #pour chaque piques
			dest = self.trouver_destinations(i)
			for j in range(len(dest)):  #pour chaque destinations
				operation = (i, dest[j])  #operation
				etatFils = self.deplacer(i, dest[j])  #self + operation -> etat_fils
				etatFils.increment_cout(operation, self)  #incrementation de l'etat fils
				triplet = (operation, etatFils, etatFils.get_cout())
				triplet_list.append(triplet)
		return triplet_list

	#if e == but
	def egal(self, but):
		if (not isinstance(but, Etat)):
			error_message = "Erreur class de but invalide ( " + str(
			 type(but)) + " ).\n Etat attendu"
			print(error_message)
		return self.get_jeu() == but.get_jeu()

	#incremente le cout uniforme de l'etat (cumul)
	def cout_uniforme(self):
		self.cout += 1

	#incremente le cout non_uniforme de l'etat (cumul)
	def cout_non_uniforme(self, cout):
		self.cout += cout

	#TODO func qui détermine le cout en fonction des cubes deplacés
	def calc_cout_non_uni(self, op):
		# coup egal au numero du cube
		pique = self.get_pique(op[0])
		cout = pique.peek()[0].chiffre
		return cout

	#choisis un cout uniforme ou non_uniforme en fonction de type_cout
	def increment_cout(self, op, etat):
		if (etat.type_cout == Cout.UNIFORME):
			self.cout_uniforme()
		else:
			self.cout_non_uniforme(etat.calc_cout_non_uni(op))
