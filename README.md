## Welcome to Accordion Solitaire
This is my submission for the Kleiner Perkins Optional Programming Challenge. I have implemented the somewhat popular solitare version "Accordian" in Python 3.5. In this document I will outline how to run the script, how to play the game as well as briefly go over my testing and design decisions.

### Entry Point
To play this game run the following command on the command line inside this directory:
```
>>> python main.py
```

### Game Explanation
The goal of the game is to create the smallest number of card piles (ideally ending up at 1!). In this single player game, the user will progresively reveal cards from the deck and strategically make moves to condense card piles if possible. The game is complete when there is only 1 card pile left or if there are no more possible moves and all cards have been reveleaed from the deck.

### Game Rules
For official game description and rules, please check out the link in the sources section.
1. Each turn the player can reveal a card from the deck and add it to the right of the cards in the tableau.
2. The player can create a "pile" from moving a card 1 or 3 spots to the LEFT. The player can make such a move in 2 conditions:
	a. the two cards have the same Rank ( i.e. Ace and Ace )
	b. the two cards have the same Suit ( i.e. Club and Club )
	The right card (and all the cards beneath it) moves ON TOP of the left card creates a pile in place.
3. If the player cannot make a move as described in rule 2, they can continue to reveal cards until this is possible.
4. If all the cards have been relieved and there are no more moves avaialble, the game is over.
5. The goal is to have the least amount of piles once the board reaches such a state as described in rule 5.

### Testing
For testing I used the framework PyTest. To run my testing files perform the following commands within this projects directory:
```
>>> cd tests/
>>> pytest -v
```
** Pytest must be installed for the testing to be run **

### Design Document
I have linked to my design document markdown file within this repository:

### Sources
Here is my main source for a comprehensive understanding of the accoridian solitaire game.
- https://www.bvssolitaire.com/rules/accordion.htm