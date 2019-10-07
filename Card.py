class Card: 
	'''
	Base class of interaction in the game. Initialization specifies the suit 
	and rank for the card
	'''

	def __init__(self, s, r):
		self.suit = s
		self.rank = r

	# Clean way to represent the cards
	def __str__(self): 
		return "[ ({}, {}) ]".format(self.suit, self.rank)