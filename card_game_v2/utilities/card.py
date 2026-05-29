import random

class Card:
    # card needs value, penalty value.
    def __init__(self, value):
        self.value = value
        # for now, have a random value for penalties
        self.penalty_amount = random.randint(1,10)
        self.played_by = None

    def __repr__(self):
        return f"{self.value}"
    def __str__(self):
        return f"{self.value}"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        else:
            return False
    def __gt__(self, other):
        if isinstance(other, Card):
            return self.value > other.value
        return NotImplemented
    def __lt__(self, other):
        if isinstance(other, Card):
            return self.value < other.value
        return NotImplemented