from abc import ABC, abstractmethod

from re import I
from threading import Thread
from board import Board
from player.Player import Player


class Game(ABC, Thread):
    def __init__(self, playerA: Player, playerB: Player):
        super().__init__()

        self.playerA = playerA
        self.playerB = playerB
        self.boardPlayerA = Board(playerA.name)
        self.boardPlayerB = Board(playerB.name)
        self.turn = 0

        self.initShips()

    def initShips(self):
        # initialisation des bateaux du joueur A
        self.boardPlayerA.addShip(self.playerA.get_ship(2))
        self.boardPlayerA.addShip(self.playerA.get_ship(3))
        self.boardPlayerA.addShip(self.playerA.get_ship(4))

        # initialisation des bateaux du joueur B
        self.boardPlayerB.addShip(self.playerB.get_ship(2))
        self.boardPlayerB.addShip(self.playerB.get_ship(3))
        self.boardPlayerB.addShip(self.playerB.get_ship(4))

        self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB)
        self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA)

    def nextTurn(self):
        if self.turn % 2 == 0:
            self.boardPlayerB.shot(self.playerA.get_shot())
            self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB)

        else:
            self.boardPlayerA.shot(self.playerB.get_shot())
            self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA)

        self.turn += 1

    def isFinished(self) -> bool:
        finished = self.boardPlayerA.is_win() or self.boardPlayerB.is_win()

        if finished:
            if not self.boardPlayerA.is_win():
                self.playerA.set_win()
                self.playerB.set_lose()
            else:
                self.playerB.set_win()
                self.playerA.set_lose()

        return finished

    def run(self):
        while not self.isFinished():
            self.nextTurn()
