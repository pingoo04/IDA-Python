import os


class Pique:
	#initialisation Pique
	def __init__(self, nb_cubes_max):
		self.nb_cubes_max = nb_cubes_max
		self.liste = []
		self.nb_cubes = 0

	def get_cube(self, ci):
		if(ci < self.nb_cubes):	
			return self.liste[ci]
		return None
		
	#retourne le premier element de la pique et sa hauteur sur la pique
	def peek(self):
		return self.liste[len(self.liste)-1], len(self.liste)-1
		
	#push la pique (pile)
	def ajouter(self, cube):
		if (self.nb_cubes < self.nb_cubes_max):
			self.liste.append(cube)
			self.nb_cubes += 1
		else:
			error_message = "Ajout impossible, pique pleine.".format(
			 os.strerror(os.error))
			print(error_message)

	#pop la pique (pile)
	def retirer(self):
		if (self.nb_cubes > 0):
			self.nb_cubes -= 1
			return self.liste.pop()
		error_message = "Retrait impossible, pique vide.".format(
		 os.strerror(os.error))
		print(error_message)

	# test si la pique est pleine
	def is_full(self):
		return (self.nb_cubes == self.nb_cubes_max)

	# test si la pique est vide
	def is_empty(self):
		return len(self.liste)==0