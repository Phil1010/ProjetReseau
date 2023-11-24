import random
from board import Board
from player.Player import Player
from ship import Ship
from shot import Shot
from message import Message

class Bot(Player):
    def __init__(self):
        super().__init__("bot")

    def get_username(self) -> str:
        return "bot"

    def get_shot(self, board: Board, message: Message) -> Shot:
        return Shot(random.randint(0, 9), random.randint(0, 9))

    def get_ship(self, board: Board, size: int) -> Ship:
        ship = Ship(random.randint(0, 9 - size), random.randint(0, 9 - size), size, random.choice(["v", "h"]))
        while not board.is_ship_position_valid(ship):
            ship = Ship(random.randint(0, 9 - size), random.randint(0, 9 - size), size, random.choice(["v", "h"]))

        return ship

    def set_win(self) -> None:
        print("win")

    def set_lose(self) -> None:
        print("lose")

    def get_gamemode(self) -> None:
        pass

    def set_grid(self, playerBoard, ennemyBoard: Board, playerA, playerB) -> None:
        pass

    def notify(self, duree: int):
        pass

    def timeout(self):
        pass

    def set_exit(self) -> None:
        pass

    def set_time(self, duration: int) -> None:
        pass

    def sendMessage(self, message: str) -> None:
        pass

    
    def get_action(self) -> Message:
        return Message("set action", "/jouer")

    def get_message(self) -> str:
        return ""
