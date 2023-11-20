import pickle
from typing import Dict
from board import Board
from message import Message
from player.Player import Player
from socket import socket

from ship import Ship
from shot import Shot


class Human(Player):
    def __init__(self, socket: socket):
        super().__init__("human")
        self.socket = socket
        self.name = self.get_username()

    def get_username(self) -> str:
        self.socket.send(pickle.dumps(Message("get username", "")) + "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        while message.content.strip() == "":
            self.socket.send(pickle.dumps(Message("get username", "")) + "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))
        return message.content

    def get_shot(self, board: Board) -> Shot:
        self.socket.send(pickle.dumps(Message("get shot", ""))+ "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        shot = pickle.loads(message.content)
        while not board.is_shot_valid(shot):
            self.socket.send(pickle.dumps(Message("get shot", ""))+ "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))
            shot = pickle.loads(message.content)
        return shot

    def get_ship(self, board: Board, size: int) -> Ship:
        self.socket.send(pickle.dumps(Message("get boat", size))+ "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        ship = pickle.loads(message.content)
        while not board.is_ship_position_valid(ship):
            self.socket.send(pickle.dumps(Message("get boat", size))+ "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))
            ship = pickle.loads(message.content)
        return ship

    def get_room(self) -> str:
        self.socket.send(pickle.dumps(Message("get room", ""))+ "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        while not (message.content == "c" or message.content == "r"):
            print("error")
            self.socket.send(pickle.dumps(Message("get room", ""))+ "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))

        return message.content

    def create_room(self, room_list) -> str:
        self.socket.send(pickle.dumps(Message("create room", ""))+ "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        while message.content in room_list:
            self.socket.send(pickle.dumps(Message("create room", ""))+ "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))

        return message.content 

    def join_room(self, room_list) -> str:
        self.socket.send(pickle.dumps(Message("show room", pickle.dumps(list(room_list.keys()))))+ "\r\n".encode())
        self.socket.send(pickle.dumps(Message("join room", ""))+ "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        while not message.content in room_list:
            self.socket.send(pickle.dumps(Message("show room", pickle.dumps(list(room_list.keys()))))+ "\r\n".encode())
            self.socket.send(pickle.dumps(Message("join room", ""))+ "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))

        return message.content

    def send_error(self, message: str) -> None:
        self.socket.send(pickle.dumps(Message("", message))+ "\r\n".encode())

    def set_win(self) -> None:
        self.socket.send(pickle.dumps(Message("end game", "Vous avez gagné"))+ "\r\n".encode())

    def set_lose(self) -> None:
        self.socket.send(pickle.dumps(Message("end game", "Vous avez perdu"))+ "\r\n".encode())

    def get_gamemode(self) -> str:
        self.socket.send(pickle.dumps(Message("get gamemode", ""))+ "\r\n".encode())
        message = pickle.loads(self.socket.recv(1024))
        while not (message.content == "s" or message.content == "m"):
            self.socket.send(pickle.dumps(Message("get gamemode", ""))+ "\r\n".encode())
            message = pickle.loads(self.socket.recv(1024))

        return message.content

        

    def set_grid(self, playerBoard, ennemyBoard: Board, playerA, playerB) -> None:
        res = playerBoard.drawHeader()
        for i in range(10):
            res += playerBoard.drawLineWithShipsAndShots(i)
            res += 10 * " "
            res += ennemyBoard.drawLineWithShots(i)
            res += "\n"

        res += "# ! ! ! ! ! ! ! ! ! ! #" + 10 * " " + "# ! ! ! ! ! ! ! ! ! ! #\n"

        res = res.replace("votre plateau",playerA.name)
        res = res.replace("plateau ennemi",playerB.name)
                
        self.socket.send(pickle.dumps(Message("set grid", res))+ "\r\n".encode())

    def notify(self, duree: int):
        self.socket.send(pickle.dumps(Message("set chronometer", duree)))

    def timeout(self):
        self.socket.send(pickle.dumps(Message("set timeout", "")))

