import sys

sys.path.append("../")

from Card import Card
from Deck import Deck
from Gameboard import Gameboard

def test_gameboard_init():
	gb = Gameboard()

	assert len(gb.board) == 2
	assert len(gb.deck.cards) == 50

	# Ensure that the cards displayed are different
	suit_check = gb.board[0].suit != gb.board[1].suit
	rank_check = gb.board[0].rank != gb.board[1].rank
	assert suit_check and rank_check

# Validation Function Tests

def test_valid_choice():
	gb = Gameboard()

	assert gb.valid_choice("y") == True
	assert gb.valid_choice("Y") == True
	assert gb.valid_choice("n") == True
	assert gb.valid_choice("N") == True

	assert gb.valid_choice("U") == False

def test_valid_number():
	gb = Gameboard()

	assert gb.valid_number(-3) == False
	assert gb.valid_number(72) == False
	assert gb.valid_number(1) == True
	assert gb.valid_number(0) == True

def test_valid_move():
	gb = Gameboard()
	board_state_1 = [Card("S", "A"), Card("S", "2")]
	board_state_2 = [Card("S", "A"), Card("C", "A")]
	board_state_3 = [Card("S", "A"), Card("C", "2"), Card("D", "3"), Card("H", "3")]
	board_state_4 = [Card("S", "A"), Card("C", "2"), Card("D", "3"), Card("S", "4")]
	board_state_5 = [Card("S", "A"), Card("C", "2"), Card("D", "3"), Card("H", "A")]

	gb.board = board_state_1

	assert gb.valid_move(1, 101) == False

	# Test 1 to the right suit move
	assert gb.valid_move(0, 1) == True
	assert gb.valid_move(0, 3) == False # Out of bounds check

	gb.board = board_state_2

	# Test 1 to the right rank move
	assert gb.valid_move(0, 1) == True
	assert gb.valid_move(0, 3) == False # Out of bounds check

	gb.board = board_state_3

	# Test with more options and valid 3 to the right
	assert gb.valid_move(0, 1) == False
	assert gb.valid_move(0, 3) == False
	assert gb.valid_move(1, 2) == False
	assert gb.valid_move(2, 3) == True

	gb.board = board_state_4

	# Test valid 3 to the right suit match
	assert gb.valid_move(0, 1) == False
	assert gb.valid_move(1, 3) == False
	assert gb.valid_move(2, 1) == False
	assert gb.valid_move(0, 3) == True

	gb.board = board_state_4

	# Test valid 3 to the right rank match
	assert gb.valid_move(0, 1) == False
	assert gb.valid_move(1, 3) == False
	assert gb.valid_move(2, 3) == False
	assert gb.valid_move(0, 3) == True







