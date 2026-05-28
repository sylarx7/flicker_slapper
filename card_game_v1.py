import random

end_score = 666
is_game_over = False
# "shuffle" deck of cards that have values from 1-100

# deck should have 100 total values
deck = []


while len(deck) < 100:
    randValue = random.randrange(1,101)

    if randValue not in deck:
        deck.append(randValue)
    

print(deck)

# cards in hand
player_hand = []
bot1_hand = []
bot2_hand = []
bot3_hand = []

# penalty in hand
player_penalty = 0
bot1_penalty = 0
bot2_penalty = 0
bot3_penalty = 0
penalty_points = [player_penalty, bot1_penalty, bot2_penalty, bot3_penalty]

# distribute cards to each player. max 10 cards each

count = 0
max_cards_per_player = 10

while count < max_cards_per_player:
    # add card to player
    player_hand.append(deck[0])
    # delete the card from deck
    deck.pop(0)
    bot1_hand.append(deck[0])
    deck.pop(0)
    bot2_hand.append(deck[0])
    deck.pop(0)
    bot3_hand.append(deck[0])
    deck.pop(0)

    count+=1

print("deck")
print(deck)

print(f"player = {player_hand}")
print(f"bot1= {bot1_hand}")
print(f"bot2 = {bot2_hand}")
print(f"bot3 = {bot3_hand}")


# add 1 card on each row to start the game
row1 = []
row2 = []
row3 = []

row1.append(deck[0])
deck.pop(0)
row2.append(deck[0])
deck.pop(0)
row3.append(deck[0])
deck.pop(0)



# game start

turn = 0

cards_played = []

while not is_game_over:
    # clear/reset cards played
    cards_played.clear()
    print("******************")
    print(f"row1 = {row1}")
    print(f"row2 = {row2}")
    print(f"row3 = {row3}")
    print("******************")
    # player choose a card to play
    print("your hand")
    print(player_hand)
    player_played = int(input("card to play > > > "))
    cards_played.append(player_played)
    # remove card played
    player_hand.remove(player_played)

    # bot turn
    bot1_played = int(random.choice(bot1_hand))
    print(f"BOT_1 played {bot1_played}")
    cards_played.append(bot1_played)
    bot1_hand.remove(bot1_played)

    bot2_played = int(random.choice(bot2_hand))
    print(f"BOT_2 played {bot2_played}")
    cards_played.append(bot2_played)
    bot2_hand.remove(bot2_played)

    bot3_played = int(random.choice(bot3_hand))
    print(f"BOT_3 played {bot3_played}")
    cards_played.append(bot3_played)
    bot3_hand.remove(bot3_played)

    # sort the cards played
    cards_played.sort()
    print(cards_played)

    # put all rows in 1 list
    rows = [row1, row2, row3]

    # check placement logic TBD
    # filter out the rows whose last value is smaller than the card played.
    # find which of the rows' last value is the closest to the card played
    for card in cards_played:
        closest_row = None
        # if lowest_difference is = 0 after all rows checked, that means that that no rows is valid
        current_lowest_difference = None
        for row in rows:
            # check each row if it is smaller than the card played
            # if it is, get get difference
            if card > row[-1]:
                difference = card - row[-1]
                # assgn it as current lowest difference
                # if the values still None; meaning this is the first instance
                if current_lowest_difference is None:
                    current_lowest_difference = difference
                    closest_row = row
                else:
                    # compare and update differences 
                    if difference < current_lowest_difference:
                        current_lowest_difference = difference
                        closest_row = row

        # add new card to the row
        # when found, if the card played is greater, then add it to the row
        if closest_row is not None:
            if len(closest_row) < 5:
                closest_row.append(card)
            # if the the number of cards in the row is greater than 5, then calculate the penalty by getting the sum of the row excluding the card played (for now, use the cards' value for penalty)
            else:
                # use the current card value for now
                row_penalty_points = sum(closest_row)
                #then clear the row, then initialize the row with the card played.
                closest_row.clear()
                closest_row.append(card)
                # add the penalty point to the player or bot
                if card == player_played:
                    player_penalty += row_penalty_points
                elif card == bot1_played:
                    bot1_penalty += row_penalty_points
                elif card == bot2_played:
                    bot2_penalty += row_penalty_points
                elif card == bot3_played:
                    bot3_penalty += row_penalty_points
        # if no row was modified, meaning the card is smaller than the last value on each row
        else:
            # if the card was played by the player
            if card == player_played:
                # row to reset
                row_chosen = int(input("Pick a row to take 1, 2 ,3:\n> > >"))
                row_penalty_points = sum(rows[row_chosen - 1])
                rows[row_chosen - 1].clear()
                rows[row_chosen - 1].append(card)
                player_penalty += row_penalty_points
            # if the card was played by 1 of the bots
            else:
                # do once since it is by the bot anyway
                bot_picked = random.randint(1,3)
                row_penalty_points = sum(rows[bot_picked - 1])
                rows[bot_picked - 1].clear()
                rows[bot_picked - 1].append(card)

                # apply penalty points to the bot who played the card
                if card == bot1_played:
                    bot1_penalty += row_penalty_points
                elif card == bot2_played:
                    bot2_penalty += row_penalty_points
                elif card == bot3_played:
                    bot3_penalty += row_penalty_points
        # repeat for all the cards played
        # repeat the whole loop until there are no more cards in hands left





    print("**TURN RESULT***")
    for row in rows:
        print(row)

    # display current penalties
    print(f"Player Penalty = {player_penalty}")
    print(f"BOT1 Penalty = {bot1_penalty}")
    print(f"BOT2 Penalty = {bot2_penalty}")
    print(f"BOT3 Penalty = {bot3_penalty}")

    current_penalties = [player_penalty, bot1_penalty, bot2_penalty, bot3_penalty]
    turn += 1
    # check if any player got 666 points then it's game over
    for penalty in current_penalties:
        if penalty >= end_score:
            # DISPLAY GAME OVER Then RESULT
            print("*****************************")
            print("GAME OVER")
            print("**SCORES**")
            print(f"Player = {player_penalty}")
            print(f"BOT1 = {bot1_penalty}")
            print(f"BOT2 = {bot2_penalty}")
            print(f"BOT3 = {bot3_penalty}")
            is_game_over = True