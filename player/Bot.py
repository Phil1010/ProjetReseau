import random
from typing import List
from board import Board
from coordinate import Coordinate
from player.Player import Player
from ship import Ship


class Bot(Player):
    def __init__(self):
        super().__init__("bot")

    def get_username(self) -> str:
        return "bot"

    def get_shot(self) -> Coordinate:
        return Coordinate(random.randint(0, 9), random.randint(0, 9))

    def get_ship(self, size: int) -> Ship:
        return Ship(random.randint(0, 9 - size), random.randint(0, 9 - size), size, random.choice(["v", "h"]))

    def set_win(self) -> None:
        print("win")

    def set_lose(self) -> None:
        print("lose")

    def get_gamemode(self) -> None:
        pass

    def set_grid(self, playerBoard, ennemyBoard: Board) -> None:
        pass