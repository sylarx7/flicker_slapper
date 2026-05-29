from utilities.deck import Deck
from utilities.player import Player



class Game:
    def __init__(self):
        self.deck = Deck(100)   #create deck
        self.deck.build()       #build the deck
        self.deck.shuffle()     #shuffle deck
        self.is_game_over = False   #game state
        self.max_card_on_hand = 10
        self.max_points = 100
        self.players = [
            Player("Player", False),
            Player("Bot-1", True),
            Player("Bot-2", True),
            Player("Bot-3", True),
        ]
        self.rows =  [
            [],
            [],
            []
        ]

    def Start(self):
        # add card to the rows to start
        for row in self.rows:
            row.append(self.deck.deal())

        # give cards to palyers
        for player in self.players:
            while len(player.hand) != self.max_card_on_hand:
                player.hand.append(self.deck.deal())

    def Round(self):
        cards_played = []

        # display the rows
        for row in self.rows:
            print(row)

        # ask palyers to play a card
        for player in self.players:
            cards_played.append(player.play_card())
        
        # sort played cards in ascending order
        cards_played.sort()

        # process placement of played cards
        # filter out the played cards
        for card in cards_played:
            # this will reset for each card played comparison
            closest_row = None
            lowest_difference = None

            # check against the last value in the row
            for row in self.rows:
                # get difference if card played is greater than the row's last value
                if card > row[-1]:
                    difference = card - row[-1]
                    # if this is the first filter, or have lower difference
                    if lowest_difference is None or difference < lowest_difference:
                        lowest_difference = difference
                        closest_row = row
            
            # process the card into the rows
            if closest_row is not None:
                # if the len of closest row is < 5 append it
                if len(closest_row) < 5:
                    closest_row.append(card)
                # row full, calculate penalty 
                else:
                    total_penalty = 0
                    # take sum of the row
                    for penalty_card in closest_row:
                        total_penalty += penalty_card.penalty_amount
                    
                    # update row
                    closest_row.clear()
                    closest_row.append(card)
                    # apply penalty
                    card.played_by.penalty_points += total_penalty

            # if closest_row is NONE; meaning no valid card to compare to
            # they have to pick from 1 of the rows
            else:
                # take the row with the lowest sum
                # applies to both human and bots
                row_with_lowest_penalty = None
                penalty_points = 999999999
                # calculte penalty points
                for row in self.rows:
                    row_sum = 0
                    # get the sum of penalty points per row
                    for penalty_card in row:
                        row_sum += penalty_card.penalty_amount
                    # update penalty points if necessary
                    if row_sum < penalty_points:
                        penalty_points = row_sum
                        row_with_lowest_penalty = row

                
                # update the row
                row_with_lowest_penalty.clear()
                row_with_lowest_penalty.append(card)

                # apply penalty points to the player
                card.played_by.penalty_points += penalty_points


        # ROUND SUMMARY
        # reset order and display current penalty points
        player_current_rankings = self.players.copy()
    
        # sort the current rankings
        # using the lambda function, it will sort the list object using their attribute
        player_current_rankings.sort(key = lambda p : p.player.penalty_points)
        
        # display rankings
        for rank, player in enumerate(player_current_rankings, start=1):
            print(f"Rank {rank} => {player.name} with {player.penalty_points} points")

        # check if game is over; a player reach max score
        if player_current_rankings[-1].penalty_points >= self.max_points:
            self.is_game_over = True