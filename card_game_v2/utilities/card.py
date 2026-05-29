import random

class Card:
    # card needs value, penalty value.
    def __init__(self, value):
        self.value = value
        # for now, have a random value for penalties
        self.penalty_amount = random.randint(1,10)
        self.played_by = None

    def __str__(self):
        return f"Card# {self.value} (PPoints = {self.penalty_amount})"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        else:
            return False