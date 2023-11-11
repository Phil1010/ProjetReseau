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
        # TODO: la vérification des tirs est pas bonne 
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
                self.socket.send("play\n".encode())
                self.socket.send(
                    "La position de tir que vous avez entrez n'est pas valide, veuillez en entrez une nouvelle.\n".encode()
                )
                message = self.socket.recv(1024).decode("utf-8")
                coords = message.split(",")

        ennemyBoard.shot(int(coords[0]), int(coords[1]))
        return ennemyBoard

    def getShip(self, board: Board, size: int) -> Ship:
        # self.socket.send("boat\n".encode())

        if size == 2:
            self.socket.send("small boat\n".encode())
        if size == 3:
            self.socket.send("medium boat\n".encode())
        if size == 4:
            self.socket.send("big boat\n".encode())

        shipJson = self.socket.recv(1024).decode("utf-8")  # demande d'un bateau
        shipDict = json.loads(shipJson)  # json -> python dict

        while True:
            try:
                int(shipDict["x"])
                int(shipDict["y"])
                # TODO: vérifier si l'orientation est bonne
                break
            except:
                self.socket.send(
                    "Le bateau ne peut pas être placé ici, la place est déjà prise ou le placement indiqué est invalide.\n".encode()
                )
                if size == 2:
                    self.socket.send("small boat\n".encode())
                if size == 3:
                    self.socket.send("medium boat\n".encode())
                if size == 4:
                    self.socket.send("big boat\n".encode())
                shipJson = self.socket.recv(1024).decode("utf-8")  # demande d'un bateau
                shipDict = json.loads(shipJson)  # json -> python dict

        ship = Ship(
            int(shipDict["x"]),
            int(shipDict["y"]),
            size,
            shipDict["orientation"],
        )

        while not board.isShipPlacable(ship):
            # TODO: pb le bateau peut être placé a moitié dans la grille et a moitié pas dans la grille 
            self.socket.send(
                "Le bateau ne peut pas être placé ici, la place est déjà prise ou le placement indiqué est invalide.\n".encode()
            )
            if size == 2:
                self.socket.send("small boat\n".encode())
            if size == 3:
                self.socket.send("medium boat\n".encode())
            if size == 4:
                self.socket.send("big boat\n".encode())

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
