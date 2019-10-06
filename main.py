from Gameboard import Gameboard

if __name__ == "__main__":
	print('''\n
		***********************************************
		*                                             *
		* Welcome to Accordian Solitaire CLI version! *
		*                                             *
		***********************************************

		                 INSTRUCTIONS:

		************************************************

		1. Each turn, the player can reveal a card from the deck and add it to the right of the cards in the tableau (display of all cards)
		2. The player can create a "pile" from moving a card in the tableau 1 or 3 spots to the LEFT. The player can make such a move in 1 of 2 conditions:
			* the two cards have the same Rank ( i.e. Ace and Ace )
			* the two cards have the same Suit ( i.e. Club and Club )
		3. The right card (and all the cards beneath it) moves ON TOP of the left card creates a pile in place.
		4. If the player cannot make a move as described in rule 2, they can continue to reveal cards until this is possible.
		5. If all the cards have been revealed and there are no more moves avaialble, the game is over.
		6. The goal is to have the least amount of piles once the board reaches such a state as described in rule 5.

		*************************************************
		                  EXAMPLE CARD:

		               [  (SUIT, RANK)  ]

		               C ===> CLUB
		               S ===> SPADE
		               H ===> HEART
		               D ===> DIAMOND

		*************************************************


		*************************************************
		       To Exit Game Early: CTRL + C + Enter
		*************************************************

		\n''')

	gb = Gameboard()

	while True:
		# Display inital state
		gb.display_state()

		# Let player choose next move
		gb.prompt_for_move()