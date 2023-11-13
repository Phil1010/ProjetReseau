from abc import ABC, abstractmethod
from threading import Thread
from board import Board
from chrono import Timer
from player.Player import Player


class Game(Thread):
    def __init__(self, playerA: Player, playerB: Player):
        super().__init__()

        self.playerA = playerA
        self.playerB = playerB
        self.boardPlayerA = Board(playerA.name)
        self.boardPlayerB = Board(playerB.name)
        self.turn = 0

        self.initShips()

    def initShips(self):
        # TODO: faire ca en plus propre
        self.boardPlayerA.addShip(self.playerA.getShip(self.boardPlayerA, 2))
        self.boardPlayerA.addShip(self.playerA.getShip(self.boardPlayerA, 3))
        self.boardPlayerA.addShip(self.playerA.getShip(self.boardPlayerA, 4))

        self.boardPlayerB.addShip(self.playerB.getShip(self.boardPlayerB, 2))
        self.boardPlayerB.addShip(self.playerB.getShip(self.boardPlayerB, 3))
        self.boardPlayerB.addShip(self.playerB.getShip(self.boardPlayerB, 4))

    def nextTurn(self):
        if self.turn % 2 == 0:
            self.boardPlayerB = self.playerA.play(self.boardPlayerA, self.boardPlayerB)

        else:
            self.boardPlayerA = self.playerB.play(self.boardPlayerB, self.boardPlayerA)

        self.turn += 1

    def isFinished(self) -> bool:
        finished = self.boardPlayerA.is_win() or self.boardPlayerB.is_win()

        if finished:
            if not self.boardPlayerA.is_win():
                self.playerA.win()
                self.playerB.lose()
            else:
                self.playerB.win()
                self.playerA.lose()

        return finished

    def drawGame(self) -> str:
        return ""
    
    def run(self):
        while not self.isFinished():
            self.nextTurn()
