from abc import ABC
from board import Board
from player.Player import Player


class Game(ABC):
    def __init__(self, playerA: Player, playerB: Player):
        self.playerA = playerA
        self.playerB = playerB
        self.boardPlayerA = Board(playerA.name)
        self.boardPlayerB = Board(playerB.name)
        self.turn = 0

        self.initShips()

    def initShips(self):
        # TODO: faire ca en plus propre
        if len(self.boardPlayerA.ships) == 0:
            self.boardPlayerA.addShip(self.playerA.getShip(1))

        if len(self.boardPlayerA.ships) == 1:
            self.boardPlayerA.addShip(self.playerA.getShip(2))

        if len(self.boardPlayerA.ships) == 2:
            self.boardPlayerA.addShip(self.playerA.getShip(3))

        try:
            if len(self.boardPlayerB.ships) == 0:
                self.boardPlayerB.addShip(self.playerB.getShip(1))
            if len(self.boardPlayerB.ships) == 1:
                self.boardPlayerB.addShip(self.playerB.getShip(2))
            if len(self.boardPlayerB.ships) == 2:
                self.boardPlayerB.addShip(self.playerB.getShip(3))

        except Exception:
            self.initShips

    def nextTurn(self):
        if self.turn % 2 == 0:
            self.boardPlayerB = self.playerA.play(self.boardPlayerA, self.boardPlayerB)
            
            print(self.boardPlayerB.drawFullBoard())
        else:
            self.boardPlayerA = self.playerB.play(self.boardPlayerB, self.boardPlayerA)

        self.turn += 1

    def isFinished(self) -> bool:
        finished = self.boardPlayerA.is_win() or self.boardPlayerB.is_win()
       
        if finished:
            if not self.boardPlayerA.is_win():
                self.playerA.win()
                self.playerB.lose()
                print("a win b lose")
            else:
                self.playerB.win()
                self.playerA.lose()
                print("b win a lose")

        

        return finished

    def drawGame(self) -> str:
        return ""
