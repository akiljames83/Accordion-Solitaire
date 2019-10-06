from Gameboard import Gameboard

if __name__ == "__main__":
	print('''\n
		***********************************************
		*											  *
		* Welcome to Accordian Solitaire CLI version! *
		*											  *
		***********************************************
		\n''')

	gb = Gameboard()

	while True:
		# Display inital state
		gb.display_state()

		# Let player choose next move
		gb.prompt_for_move()

	print('''\n
		***********************************************
		*              Thanks for Playing!            *
		***********************************************
		\n''')