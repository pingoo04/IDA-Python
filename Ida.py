class Ida:
	#initialisation Ida
	def __init__(self, but):
		self.but = but

	#get but
	def get_but(self):
		return self.but

	#si but attein vrai sinon faux
	def estBut(self, e):
		return e.egal(self.get_but())
