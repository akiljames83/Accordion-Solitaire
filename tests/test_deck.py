import sys

sys.path.append("../")

from Deck import Deck

def test_init():
	deck = Deck()

	# Ensure 52 cards are created
	assert len(deck.cards) == 52

def test_deck_shuffle():
	deck = Deck()

	for i, card in enumerate(deck.cards):
		print(card, end = " ")
		if (i % 5) == 0:
			print("\n")


	hearts, diamonds, clubs, spades = set(), set(), set(), set()
	for card in deck.cards:
		# Ensure all cards are unique
		if (card.suit == "H"):
			assert (card.rank in hearts) == False
			hearts.add(card.rank)
		elif (card.suit == "D"):
			assert (card.rank in diamonds) == False
			diamonds.add(card.rank)
		elif (card.suit == "C"):
			assert (card.rank in clubs) == False
			clubs.add(card.rank)
		elif (card.suit == "S"):
			assert (card.rank in spades) == False
			spades.add(card.rank)
		else:
			raise("Undefined Suit")

	# Ensure there are 13 cards of each suit
	assert (len(diamonds)) == 13
	assert (len(clubs)) == 13
	assert (len(hearts)) == 13
	assert (len(spades)) == 13

def test_deck_draw():
	deck = Deck()
	first_card = deck.cards[0]

	# Ensure card is removed with draw func
	assert len(deck.cards) == 52
	draw_card = deck.draw()
	assert len(deck.cards) == 51

	# Ensure the value returned is of type card and that it is the 
	# same as first value in the deck.cards array
	assert type(draw_card) == type(first_card)
	assert draw_card.suit == first_card.suit
	assert draw_card.rank == first_card.rank

	# Remove all cards from the deck
	for i in range(51):
		deck.draw()

	# Ensure that an empty deck returns a bool value of false
	empty_draw = deck.draw()
	assert isinstance(empty_draw, bool) == True
	assert empty_draw == False