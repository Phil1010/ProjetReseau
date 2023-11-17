from abc import ABC, abstractmethod

from re import I
from threading import Thread
import threading
from board import Board
from chrono import Chronometre, Timer
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
        
        self.stop_chronometer = threading.Event()
        self.chronometer = Chronometre(self.playerA, self.playerB, self.stop_chronometer).start()

    def initShips(self):
        # initialisation des bateaux du joueur A
        self.boardPlayerA.addShip(self.playerA.get_ship(self.boardPlayerA, 2))
        self.boardPlayerA.addShip(self.playerA.get_ship(self.boardPlayerA, 3))
        self.boardPlayerA.addShip(self.playerA.get_ship(self.boardPlayerA, 4))

        # initialisation des bateaux du joueur B
        self.boardPlayerB.addShip(self.playerB.get_ship(self.boardPlayerB, 2))
        self.boardPlayerB.addShip(self.playerB.get_ship(self.boardPlayerB, 3))
        self.boardPlayerB.addShip(self.playerB.get_ship(self.boardPlayerB, 4))

        self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB)
        self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA)


    def nextTurn(self):
        if self.turn % 2 == 0:
            Timer(self.playerA, 20).start() 
            self.boardPlayerB.shot(self.playerA.get_shot(self.boardPlayerB))
            self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB)

        else:
            Timer(self.playerB, 20).start() 
            self.boardPlayerA.shot(self.playerB.get_shot(self.boardPlayerA))
            self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA)

        self.turn += 1

    def isFinished(self) -> bool:
        finished = self.boardPlayerA.is_win() or self.boardPlayerB.is_win()

        if finished:
            self.stop_chronometer.set()

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
