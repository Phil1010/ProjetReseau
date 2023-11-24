
import pickle
from typing import Dict
from board import Board
from message import Message
from player.Human import Human
from socket import socket

from ship import Ship
from shot import Shot



class Spectator():
    def __init__(self, socket: socket):
        self.socket = socket

    def set_grid(self, playerBoard, ennemyBoard: Board, playerA, playerB) -> None:
        res = playerBoard.drawHeader()
        for i in range(10):
            res += playerBoard.drawLineWithShipsAndShots(i)
            res += 10 * " "
            res += ennemyBoard.drawLineWithShipsAndShots(i)
            res += "\n"

        res += "# ! ! ! ! ! ! ! ! ! ! #" + 10 * " " + " # ! ! ! ! ! ! ! ! ! ! #\n"

        res = res.replace("votre plateau",playerA.name)
        res = res.replace("plateau ennemi",playerB.name)
                
        self.socket.send(pickle.dumps(Message("set grid", res))+ "\r\n".encode())

    def set_time(self, duration: int) -> None:
        self.socket.send(pickle.dumps(Message("set time", str(duration))))


    def sendMessage(self, message: str) -> None:
        self.socket.send(pickle.dumps(Message("send message", message)))
