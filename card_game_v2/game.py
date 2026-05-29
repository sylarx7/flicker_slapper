from utilities.deck import Deck
from utilities.player import Player



class Game:
    def __init__(self):
        self.deck = Deck(100)   #create deck
        self.deck.build()       #build the deck
        self.deck.shuffle()     #shuffle deck
        self.is_game_over = False   #game state
        self.players = [
            Player("Player", False),
            Player("Bot-1", True),
            Player("Bot-2", True),
            Player("Bot-3", True),
        ]
        self.max_card_on_hand = 10
        self.rows =  [
            [],
            [],
            []
        ]

    def Start(self):
        # add card to the rows to start
        for row in self.rows:
            row.append(self.deck.deal())
        # display row
        for row in self.rows:
            print(row)

        # give cards to palyers
        for player in self.players:
            while len(player.hand) != self.max_card_on_hand:
                player.hand.append(self.deck.deal())

