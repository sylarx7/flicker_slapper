import random

class Player:
    # needs name, whether player is bot, their card on hand, penalty points
    def __init__(self, name, is_bot):
        self.name = name
        self.is_bot = is_bot
        self.hand = []
        self.penalty = 0

    def play_card(self):
        card_played = None
        if self.is_bot:
            # pick random card on hand
            card_played = random.choice(self.hand)

        else:
            # if human player, display current hand
            print("your hand")
            print(self.hand)
            card_played = int(input("Pick card to play --> "))
        
        # remove card from hand
        self.hand.remove(card_played)
        # display card played
        print(f"{self.name} played -> {card_played}")

    def __str__(self):
        return f"{self.name} joins the game"
    
