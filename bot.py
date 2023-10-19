import board
import ship
import player
import random


class Bot:
    def __init__(self, board):
        self.board = board

    def add_ship_bot(self):
        random_direction = random.choice(["h", "v"])
        random_coordonnees = random.randint(0, 5)

        try:
            if len(self.board.ships) == 0:
                self.board.add_ship(
                    ship.Ship(
                        random_coordonnees, random_coordonnees, 2, random_direction
                    )
                )
            elif len(self.board.ships) == 1:
                self.board.add_ship(
                    ship.Ship(
                        random_coordonnees, random_coordonnees, 3, random_direction
                    )
                )
            elif len(self.board.ships) == 2:
                self.board.add_ship(
                    ship.Ship(
                        random_coordonnees, random_coordonnees, 4, random_direction
                    )
                )
        except Exception:
            self.add_ship_bot()

    def shot(self):
        random_x = random.randint(0, 9)
        random_y = random.randint(0, 9)
        self.board.shot(random_x, random_y)
