from abc import ABC, abstractmethod
from operator import is_

from re import I
from threading import Thread
import threading
from board import Board
from chrono import Chronometre, Timer
from player.Player import Player
import random
import time


class Game(ABC, Thread):
    def __init__(self, playerA: Player, playerB: Player):
        super().__init__()
        
        self.spectators = []
        self.playerA = playerA
        self.playerB = playerB
        self.boardPlayerA = Board(playerA.name)
        self.boardPlayerB = Board(playerB.name)
        self.turn = 0

        self.initShips()
        self.stop_timer = threading.Event()
        self.stop_chronometer = threading.Event()
        self.chronometer = Chronometre(self.playerA, self.playerB, self.stop_chronometer).start()

    def initShips(self):
        # initialisation des bateaux du joueur A
        self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)
        self.boardPlayerA.addShip(self.playerA.get_ship(self.boardPlayerA, 2))
        self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)
        self.boardPlayerA.addShip(self.playerA.get_ship(self.boardPlayerA, 3))
        self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)
        self.boardPlayerA.addShip(self.playerA.get_ship(self.boardPlayerA, 4))
        self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)

        # initialisation des bateaux du joueur B
        self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA, self.playerB, self.playerA)
        self.boardPlayerB.addShip(self.playerB.get_ship(self.boardPlayerB, 2))
        self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA, self.playerB, self.playerA)
        self.boardPlayerB.addShip(self.playerB.get_ship(self.boardPlayerB, 3))
        self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA, self.playerB, self.playerA)
        self.boardPlayerB.addShip(self.playerB.get_ship(self.boardPlayerB, 4))
        self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA, self.playerB, self.playerA)


    def nextTurn(self):
        print("CA COMMENCE")
        self.stop_timer = threading.Event()
        if self.turn % 2 == 0:
            t = Timer(self.playerA, 60, self.stop_timer, self.spectators)
            t.start()
            
            message = self.playerA.get_action()

            while message.action == "send message":
                message = self.playerA.get_message(message)
                self.broadcastMessage(self.playerA.name + " :: " + message)
                message = self.playerA.get_action()

            if message.action == "set shot":
                shot = self.playerA.get_shot(self.boardPlayerB, message)
                self.stop_timer.set()
                if not t.is_alive():
                    shot.coordinate.x = random.randint(0, 9)
                    shot.coordinate.y = random.randint(0, 9)

                self.boardPlayerB.shot(shot)
                self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA, self.playerB, self.playerA)
                self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)

        else:
            t = Timer(self.playerB, 60, self.stop_timer, self.spectators)
            t.start()
            
            message = self.playerB.get_action()

            while message.action == "send message":
                message = self.playerB.get_message(message)
                self.broadcastMessage(self.playerB.name + " :: " + message)
                message = self.playerB.get_action()

            if message.action == "set shot":
                shot = self.playerB.get_shot(self.boardPlayerA, message)
                self.stop_timer.set()
                if not t.is_alive():
                    shot.coordinate.x = random.randint(0, 9)
                    shot.coordinate.y = random.randint(0, 9)

                self.boardPlayerA.shot(shot)
                self.playerA.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)
                self.playerB.set_grid(self.boardPlayerB, self.boardPlayerA, self.playerB, self.playerA)
        
        for spectator in self.spectators:
            spectator.set_grid(self.boardPlayerA, self.boardPlayerB, self.playerA, self.playerB)

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
            
            time.sleep(1)
            self.playerA.set_exit()
            self.playerB.set_exit()

        return finished

    def run(self):
        while not self.isFinished():
            self.nextTurn()

    def broadcastMessage(self, message: str) -> None:
        self.playerA.sendMessage(message)
        self.playerB.sendMessage(message)
        for spectator in self.spectators:
            spectator.sendMessage(message)
