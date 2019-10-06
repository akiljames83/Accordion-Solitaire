import random

from Card import Card

class Deck:
    '''
    Class that specifies the deck of cards to be dealt to the player
    and the functionality for it (such as shuffling and drawing cards).
    '''

    # Immutable state variables
    suits = ("H", "D", "C", "S")
    ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")

    def __init__(self):
        self.cards = list()
        self.make_cards()
        self.shuffle()

    def make_cards(self):  # Deck.cards is a list of all 52 cards
        for s in (self.suits):
            for r in (self.ranks):
                self.cards.append(Card(s, r))
                
    def shuffle(self):  # Shuffles the deck in place
        random.shuffle(self.cards)

    def draw(self):  # Draws the first card from the deck and returns it
        if (not len(self.cards)):
            return None
        temp_card = self.cards[0]
        del self.cards[0]
        return (temp_card)