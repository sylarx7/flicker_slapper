import random

class Card:
    # card needs value, penalty value.
    def __init__(self, value):
        self.value = value
        # for now, have a random value for penalties
        self.penalty = random.randint(1,10)
        self.played_by = None

    def __str__(self):
        return f"Card# {self.value} (PP{self.penalty})"
    
    def __eq__(self, other):
        if isinstance(other, Card):
            return self.value == other.value
        else:
            return False