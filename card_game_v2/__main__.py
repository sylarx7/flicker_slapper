from .game import Game
if __name__ == "__main__":
    g = Game()
    g.PlayGame()


# NOTE
# this version doesnt not include input validation for user meaning
#   that it will crash if user played a card that is not present
#   in their current hand.
# Reason is that this will be ported to unity anyway where the game will be polished more.