import random
from utilities.card import Card

class Deck:
    def __init__(self, max_number_of_cards):
        self.deck = []
        self.max_number_of_cards = max_number_of_cards
    
    def __str__(self):
        return f"{self.deck}"
    
    #  METHODS
    # create a deck with 100 cards
    def build(self):
        # starting value
        value = 1
        while len(self.deck) != self.max_number_of_cards:
            # create card with increasing value
            card = Card(value)
            self.deck.append(card)
            value += 1


    def shuffle(self):
        random.shuffle(self.deck)

    # distribute card
    def deal(self):
        # get the last card from the deck
        card = self.deck[-1]
        # remove said card from the deck
        self.deck.pop(-1)
        # return card
        return card