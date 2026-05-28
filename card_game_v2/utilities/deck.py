import random
from utilities.card import Card

class Deck:
    def __init__(self):
        self.deck = []
    
    def __str__(self):
        return f"{self.deck}"