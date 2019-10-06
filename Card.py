
class Card: # Base class of interaction in the game

	def __init__(self, s, r):
		self.suit = s
		self.rank = r

	# Clean way to represent the cards
	def __str__(self): 
		return "		Card: [{}, {}]	".format(self.suit, self.rank)