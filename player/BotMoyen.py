import random
from board import Board
from player.Player import Player
from ship import Ship
from shot import Shot
from message import Message


class BotMoyen(Player):
    def __init__(self):
        super().__init__("bot moyen")
        self.last_shot = Shot(0, 0)
        self.last_shot_ok = False

    def get_username(self) -> str:
        return "bot moyen"

    def get_shot(self, board: Board, message: Message) -> Shot:
        shot = Shot(0, 0)
        if self.last_shot_ok:
            coo = self.last_shot.coordinate
            randomx = random.choice([-1, 0, 1])
            coo.x += randomx

            if randomx == 0:
                coo.y += random.choice([-1, 1])
            else:
                coo.y += 0

            shot.coordinate.x = coo.x
            shot.coordinate.y = coo.y

            while not board.is_shot_valid(shot):
                coo = self.last_shot.coordinate
                randomx = random.choice([-1, 0, 1])
                coo.x += randomx

                if randomx == 0:
                    coo.y += random.choice([-1, 1])
                else:
                    coo.y += 0

                shot.coordinate.x = coo.x
                shot.coordinate.y = coo.y

            if board.grid[coo.y][coo.x] == "*":
                self.last_shot_ok = True
            else:
                self.last_shot_ok = False

            self.last_shot = shot

            return self.last_shot

        else:
            shot.coordinate.x = random.randint(0, 5)
            shot.coordinate.y = random.randint(0, 5)
            while not board.is_shot_valid(shot):
                shot.coordinate.x = random.randint(0, 5)
                shot.coordinate.y = random.randint(0, 5)

            if board.grid[shot.coordinate.y][shot.coordinate.x] == "*":
                self.last_shot_ok = True

            else:
                self.last_shot_ok = False

            self.last_shot = shot
            return shot

    def get_ship(self, board: Board, size: int) -> Ship:
        ship = Ship(
            random.randint(0, 9 - size),
            random.randint(0, 9 - size),
            size,
            random.choice(["v", "h"]),
        )
        while not board.is_ship_position_valid(ship):
            ship = Ship(
                random.randint(0, 9 - size),
                random.randint(0, 9 - size),
                size,
                random.choice(["v", "h"]),
            )

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
        return Message("set shot", "/jouer")

    def get_message(self) -> str:
        return ""
