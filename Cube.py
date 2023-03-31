def cube_equals(c1, c2):
	if( (c1==None)^(c2==None) ):
		return False
	elif(c1==None and c2==None):
		return True
	return c2.chiffre == c1.chiffre and c2.couleur == c1.couleur

class Cube:
	#initialisation Cube
	def __init__(self, chiffre):
		self.chiffre = chiffre
		self.couleur = None