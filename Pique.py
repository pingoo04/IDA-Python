class Pique:

	def __init__(self, nb_cubes_max):
		self.nb_cubes_max = nb_cubes_max
		self.liste = []
		self.nb_cubes = 0

	def ajouter(self, cube):
		if (self.nb_cubes < self.nb_cubes_max):
			self.liste.append(cube)
			self.nb_cubes += 1
		else:
			error_message = "Ajout impossible, pique pleine.".format(
			 os.strerror(os.errno))
			print(error_message)

	def retirer(self):
		if (self.nb_cubes > 0):
			self.nb_cubes -= 1
			return self.liste.pop()
		error_message = "Retrait impossible, pique vide.".format(
		 os.strerror(os.errno))
		print(error_message)

	def is_full(self):
		return (self.nb_cubes == self.nb_cubes_max)
