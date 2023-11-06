import json
from typing import List
from board import Board
from player.Player import Player
from socket import socket

from ship import Ship


class Human(Player):
    def __init__(self, socket: socket):
        super().__init__("human")
        self.socket = socket
        self.name = self.socket.recv(1024).decode("utf-8")

    def play(self, playerBoard: Board, ennemyBoard: Board) -> Board:
        self.socket.send("play".encode())

        res = playerBoard.drawHeader()
        for i in range(10):
            res += playerBoard.drawLineWithShipsAndShots(i)
            res += 10 * " "
            res += ennemyBoard.drawLineWithShots(i)
            res += "\n"

        res += "# - - - - - - - - - - #" + 10 * " " + "# - - - - - - - - - - #\n"

        self.socket.send(res.encode())

        message = self.socket.recv(1024).decode("utf-8")
        coords = message.split(",")
        ennemyBoard.shot(int(coords[0]), int(coords[1]))
        return ennemyBoard

    def getShip(self, size: int) -> Ship:
        shipJson = self.socket.recv(1024).decode("utf-8")  # demande d'un bateau
        shipDict = json.loads(shipJson)  # json -> python dict
        print("bateau recu", shipDict)
        return Ship(
            int(shipDict["x"]),
            int(shipDict["y"]),
            shipDict["size"],
            shipDict["orientation"],
        )
    
    def win(self):
        self.socket.send("Vous avez gagné !".encode())

    def lose(self):
        self.socket.send("Vous avez perdu !".encode()) 
