import json
import pickle
import time
from typing import List
from board import Board
from coordinate import Coordinate
from message import Message
from player.Player import Player
from socket import socket

from ship import Ship


class Human(Player):
    def __init__(self, socket: socket):
        super().__init__("human")
        self.socket = socket
        self.name = self.get_username()

    def get_username(self) -> str:
        self.socket.send(pickle.dumps(Message("get username", "")) + "\r\n".encode())
        return pickle.loads(self.socket.recv(1024)).content

    def get_shot(self) -> Coordinate:
        self.socket.send(pickle.dumps(Message("get shot", ""))+ "\r\n".encode())
        return pickle.loads(pickle.loads(self.socket.recv(1024)).content)

    def get_ship(self, size: int) -> Ship:
        self.socket.send(pickle.dumps(Message("get boat", size))+ "\r\n".encode())
        s = pickle.loads(pickle.loads(self.socket.recv(1024)).content)
        return s

    def get_room(self) -> str:
        self.socket.send(pickle.dumps(Message("get room", ""))+ "\r\n".encode())
        return pickle.loads(self.socket.recv(1024)).content

    def create_room(self) -> str:
        self.socket.send(pickle.dumps(Message("create room", ""))+ "\r\n".encode())
        return pickle.loads(self.socket.recv(1024)).content

    def join_room(self, rooms) -> str:
        self.socket.send(pickle.dumps(Message("show room", pickle.dumps(list(rooms.keys()))))+ "\r\n".encode())
        self.socket.send(pickle.dumps(Message("join room", ""))+ "\r\n".encode())
        return pickle.loads(self.socket.recv(1024)).content

    def send_error(self, message: str) -> str:
        self.socket.send(pickle.dumps(Message("", message))+ "\r\n".encode())

    def set_win(self) -> None:
        self.socket.send(pickle.dumps(Message("end game", "Vous avez gagné"))+ "\r\n".encode())

    def set_lose(self) -> None:
        self.socket.send(pickle.dumps(Message("end game", "Vous avez perdu"))+ "\r\n".encode())

    def get_gamemode(self) -> str:
        self.socket.send(pickle.dumps(Message("get gamemode", ""))+ "\r\n".encode())
        return pickle.loads(self.socket.recv(1024)).content
        

    def set_grid(self, playerBoard, ennemyBoard: Board) -> None:
        res = playerBoard.drawHeader()
        for i in range(10):
            res += playerBoard.drawLineWithShipsAndShots(i)
            res += 10 * " "
            res += ennemyBoard.drawLineWithShots(i)
            res += "\n"

        res += "# - - - - - - - - - - #" + 10 * " " + "# - - - - - - - - - - #\n"

        self.socket.send(pickle.dumps(Message("set grid", res))+ "\r\n".encode())

    def duration(self, duree: int):
        pass
