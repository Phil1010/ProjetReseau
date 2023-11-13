import random
from typing import List
from board import Board
from player.Player import Player
from ship import Ship


class Bot(Player):
    def __init__(self):
        super().__init__("bot")

    def play(self, playerBoard: Board, ennemyBoard: Board) -> Board:
        ennemyBoard.shot(random.randint(0, 9), random.randint(0, 9))
        return ennemyBoard

    def getShip(self, board: Board, size: int) -> Ship:
        orientation = random.choice(["h", "v"])
        randomX = random.randint(0, 10 - 1 - size)
        randomY = random.randint(0, 10 - 1 - size)
        ship = Ship(randomX, randomY, size, orientation)
        while not board.isShipPlacable(ship):
            orientation = random.choice(["h", "v"])
            randomX = random.randint(0, 10 - 1 - size)
            randomY = random.randint(0, 10 - 1 - size)
            ship = Ship(randomX, randomY, size, orientation)

        return ship

    def win(self) -> None:
        print("bot win!")

    def lose(self) -> None:
        print("bot lose!")