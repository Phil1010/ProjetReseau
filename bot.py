import board
import ship
import player
import random


class Bot:
    playerBot = player.Player("Bot", board.Board())
    random_direction = random.choice(["horizontal", "vertical"])

    if random_direction == "horizontal":
        random_coordonnees = random.randint(0, 5)
    if random_direction == "vertical":
        random_coordonnees = random.randint(0, 5)

    random_size = random.choice([2, 3, 4])

    playerBot.board.add_ship(
        ship.Ship(random_coordonnees, random_coordonnees, random_size, random_direction)
    )

    playerBot.board.add_ship(
        ship.Ship(random_coordonnees, random_coordonnees, random_size, random_direction)
    )

    playerBot.board.add_ship(
        ship.Ship(random_coordonnees, random_coordonnees, random_size, random_direction)
    )
