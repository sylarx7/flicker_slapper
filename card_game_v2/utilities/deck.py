import random
from utilities.card import Card

class Deck:
    def __init__(self):
        self.deck = []
    
    def __str__(self):
        return f"{self.deck}"
    
    #  METHODS
    # create a deck with 100 cards
    def build(self):
        # starting value
        value = 1
        while len(self.deck) != 100:
            # create card with increasing value
            card = Card(value)
            self.deck.append(card)
            value += 1


    def shuffle(self):
        random.shuffle(self.deck)

