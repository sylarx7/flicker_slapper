import random

class Player:
    # needs name, whether player is bot, their card on hand, penalty points
    def __init__(self, name, is_bot):
        self.name = name
        self.is_bot = is_bot
        self.hand = []
        self.penalty_points = 0

    def play_card(self):
        chosen_input = None
        card_played = None
        if self.is_bot:
            # pick random card on hand
            chosen_input = random.choice(self.hand)

        else:
            # if human player, display current hand
            print("your hand")
            print(self.hand)
            chosen_input = int(input("Pick card to play --> "))
        
        # remove card from hand
        for card in self.hand:
            if card.value == chosen_input:
                card_played = card
                self.hand.remove(card)
                break

        # display card played
        print(f"{self.name} played -> {card_played}")
        
        card.played_by = self
        return card_played

    def __str__(self):
        return f"{self.name} joins the game"
    
