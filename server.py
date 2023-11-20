import pickle
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import threading
from typing import List
from games.MultiplayerGame import MultiplayerGame
from games.SoloGame import SoloGame
from message import Message
from player.Human import Human


class HandleClient(Thread):
    def __init__(self, client_socket: socket, playerList: List, room_list):
        super().__init__()
        self.playerList = playerList
        self.room_list = room_list
        self.client_socket = client_socket

    def pvp(self, humanA, humanB: Human):
        game = MultiplayerGame(humanA, humanB)
        game.start()

    def solo(self, human: Human):
        game = SoloGame(human)
        game.start()

    def run(self):
        self.human = Human(self.client_socket)
        self.playerList.append(self.human)

        gamemode = self.human.get_gamemode()
        
        if gamemode == "s":
            self.solo(self.human)
        elif gamemode == "m":
            room = self.human.get_room()
            if room == "c":
                room_name = self.human.create_room(self.room_list)
                self.room_list[room_name] = [self.human]

            elif room == "r":
                room_name = self.human.join_room(self.room_list)
                self.room_list[room_name].append(self.human)

                if len(self.room_list[room_name]) == 2:
                    self.pvp(self.room_list[room_name][0], self.room_list[room_name][1])
                    self.room_list.pop(room_name, None)

            

class Server():
    def __init__(self, host, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((host, port))
        self.clientList = []
        self.room_list = {}

    def run(self):
        self.socket.listen(2)
        while True:
            client_socket, client_address = self.socket.accept()
            handler = HandleClient(client_socket, self.clientList, self.room_list)
            handler.start()

        client_socket.close()
        server_socket.close()



s = Server("127.0.0.1", 12345)
s.run()
