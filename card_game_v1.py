import random
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

while turn < max_cards_per_player:
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






    print("**TURN RESULT***")
    for row in rows:
        print(row)

    # display current penalties
    print(f"Player Penalty = {player_penalty}")
    print(f"BOT1 Penalty = {bot1_penalty}")
    print(f"BOT2 Penalty = {bot2_penalty}")
    print(f"BOT3 Penalty = {bot3_penalty}")

    turn += 1