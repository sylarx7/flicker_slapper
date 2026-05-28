class Player:
    # needs name, whether player is bot, their card on hand, penalty points
    def __init__(self, name, is_bot):
        self.name = name
        self.is_bot = is_bot
        self.hand = []
        self.penalty = 0


    def __str__(self):
        return f"{self.name} joins the game"
    
