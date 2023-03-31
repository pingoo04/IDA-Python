class Ida:
	#initialisation Ida
	def __init__(self, but):
		self.but = but

	#get but
	def get_but(self):
		return self.but

	#si but attein vrai sinon faux
	def estBut(self, etat):
		return etat.egal(self.get_but())

	
	def g(self, etat):
		return etat.get_cout()

	def h(self, etat):
		return etat.nombre_Mal_Mis(self.but)
	
	def heuristique(self, etat):
		return self.g(etat)+self.h(etat)