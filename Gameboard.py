from sys import exit

from Deck import Deck
from Card import Card

class Gameboard:
	'''
	Class for the gameboard's state. Central controller for the application
	'''

	# State variables
	ROW_LENGTH = 4
	NO_MORE_CARDS = False

	def __init__(self):
		self.deck = Deck()
		self.board = list()
		for _ in range(2):
			self.board.append(self.deck.draw())

	def display_state(self):
		''' 
		Display the new state of the board when a card is added
		or when a move is made
		'''
		print('''
			              GAME STATE
			''')

		for i, card in enumerate(self.board):
			if not (i % self.ROW_LENGTH):
				print("\n\n		", end="")
			print("{}. {}\t".format(i+1, card), end= "")

		print("\n")

	def prompt_for_move(self): 
		'''
		Main entry point for game loop
		'''

		# Check to see if no more cards in deck and one pile remains
		if (self.NO_MORE_CARDS and len(self.board) == 1):
			print('''
					*******************************************
					*			   !!CONGRATULATIONS!!        *
					*               YOU WON THE GAME          *
					*******************************************
				''')

			exit()

		# Check to see there are cards in deck but only one pile on the board
		elif (not self.NO_MORE_CARDS and len(self.board) == 1):
			print("\n		Updating board...\n")
			self.draw_card_from_deck()
			self.display_state()

		print("		Would you like to move a pile? (y/n)", end = "    ")
		choice = input().strip()

		# Ensure a valid input was given
		while (not self.valid_choice(choice)):
			print("\n		Please provide a valid input...\n")
			print("		Would you like to move a pile? (y/n)", end = "    ")
			choice = input().strip()

		# Allow player to make a new move if requested
		if (choice == 'y' or choice == 'Y'):
			self.make_a_move()
			return

		# Otherwise, draw new card for the player
		self.draw_card_from_deck()

	def draw_card_from_deck(self):
		# Draw new card
		card_drawn = self.deck.draw()
		if (not card_drawn):
			self.NO_MORE_CARDS = True
			print("\n 	No more cards to draw! You can now only make moves\n")
		else:
			self.board.append(card_drawn)

	def make_a_move(self):
		'''
		Recursive function for player to make a pile move
		'''
		print("		Which card would you like to create a pile with? (input number or Q to quit)", end = "	")
		card_choice = input().strip()

		if (card_choice == "q" or card_choice == "Q"):
			return

		card_choice = string_to_int(card_choice)

		# Ensure a valid number input was given
		while (not self.valid_number(card_choice)):
			print("\n		Please provide a valid input...\n")
			print("		Which card would you like to create a pile with? (input number or Q to quit)", end = "	")

			card_choice = input().strip()

			if (card_choice == "q" or card_choice == "Q"):
				return

			card_choice = string_to_int(card_choice)


		card_choice -= 1

		print("		Would you like to collapse 1 to the right (Enter 1) or 3 to the right (Enter 3)? (1 or 3)", end = "	")
		
		move_choice = string_to_int(input().strip())

		# Ensure a valid choice was given
		while (move_choice != 1 and move_choice != 3):
			print("\n		Please provide a valid input...\n")
			print("		Would you like to collapse 1 to the right (Enter 1) or 3 to the right (Enter 3)? (1 or 3)", end = "	")

			move_choice = string_to_int(input().strip())

		new_card = card_choice + move_choice
		if (self.valid_move(card_choice, new_card)):
			self.board[card_choice] = self.board[new_card]
			del self.board[new_card]

			print("\n 		Successful move made! Here is the updated board: \n")

			self.display_state()
			self.prompt_for_move()
			return

		else:
			print("\n		Invalid move! Try again.\n")
			self.make_a_move()

	def valid_choice(self, choice):
		if (choice == 'y' or choice == 'Y' or choice == 'n' or choice == 'N'):
			return True
		return False

	def valid_number(self, number):
		if ((number > -1) and (number <= len(self.board) - 1)):
			return True
		return False

	def valid_move(self, card_choice, new_card):
		if (new_card >= len(self.board)):
			return False
		if (self.board[new_card].suit == self.board[card_choice].suit):
			return True
		if (self.board[new_card].rank == self.board[card_choice].rank):
			return True
		return False

# Helper function to ensure type conversion for string to int dosent
# throw an exception
def string_to_int(number):
	try:
		res = int(number)
	except ValueError:
		res = -1
	return res 

