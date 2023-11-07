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

        while True:
            try:
                int(coords[0])
                int(coords[1])
                print("coords ok")

                if not ennemyBoard.isShotPositionValid(int(coords[0]), int(coords[1])):
                    self.socket.send("play\n".encode())
                    self.socket.send(
                        "La position de tir que vous avez entrez n'est pas valide, veuillez en entrez une nouvelle.\n".encode()
                    )
                    message = self.socket.recv(1024).decode("utf-8")
                    coords = message.split(",")

                else:
                    break

            except Exception:
                print("a")
                self.socket.send("play\n".encode())
                print("b")
                self.socket.send(
                    "La position de tir que vous avez entrez n'est pas valide, veuillez en entrez une nouvelle.\n".encode()
                )
                print("c")
                message = self.socket.recv(1024).decode("utf-8")
                print("d")
                coords = message.split(",")

        ennemyBoard.shot(int(coords[0]), int(coords[1]))
        return ennemyBoard

    def getShip(self, board: Board, size: int) -> Ship:
        self.socket.send("boat".encode())
        shipJson = self.socket.recv(1024).decode("utf-8")  # demande d'un bateau
        shipDict = json.loads(shipJson)  # json -> python dict

        while True:
            try:
                int(shipDict["x"])
                int(shipDict["y"])
                break
            except:
                self.socket.send(
                    "Le bateau ne peut pas être placé ici, la place est déjà prise ou le placement indiqué est invalide.\n".encode()
                )
                self.socket.send("boat\n".encode())
                shipJson = self.socket.recv(1024).decode("utf-8")  # demande d'un bateau
                shipDict = json.loads(shipJson)  # json -> python dict

        ship = Ship(
            int(shipDict["x"]),
            int(shipDict["y"]),
            size,
            shipDict["orientation"],
        )

        while not board.isShipPlacable(ship):
            self.socket.send(
                "Le bateau ne peut pas être placé ici, la place est déjà prise ou le placement indiqué est invalide.\n".encode()
            )
            self.socket.send("boat\n".encode())

            shipJson = self.socket.recv(1024).decode("utf-8")  # demande d'un bateau
            shipDict = json.loads(shipJson)  # json -> python dict
            ship = Ship(
                int(shipDict["x"]),
                int(shipDict["y"]),
                size,
                shipDict["orientation"],
            )

        return ship

    def win(self):
        self.socket.send("Vous avez gagné !".encode())

    def lose(self):
        self.socket.send("Vous avez perdu !".encode())
