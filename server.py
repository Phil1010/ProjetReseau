from http import client
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from typing import List
from games.MultiplayerGame import MultiplayerGame
from games.SoloGame import SoloGame
from player.Human import Human
from chrono import Timer


class HandleClient(Thread):
    def __init__(self, human: Human, playerList: List):
        super().__init__()
        self.human = human
        self.playerList = playerList

    def pvp(self, humanA, humanB: Human):
        game = MultiplayerGame(humanA, humanB)
        game.start()

    def solo(self, human: Human):
        game = SoloGame(human)
        game.start()

    def run(self):
        gamemode = self.human.getGamemode()
        print("gamemode == s", gamemode == "s")
        if gamemode == "s":
            print("solo")
            self.solo(self.human)
        elif gamemode == "m":
            if len(self.playerList) == 2:
                self.pvp(self.playerList[0], self.playerList[1])
                self.playerList.clear()


class Server():
    def __init__(self, host, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((host, port))

        self.clientList = []

    def run(self):
        self.socket.listen(2)
        while True:
            client_socket, client_address = self.socket.accept()

            human = Human(client_socket)
            self.clientList.append(human)
            handler = HandleClient(human, self.clientList)
            handler.start()


            # print(len(self.clientList))
            # if len(self.clientList) == 2:
            #     self.pvp(self.clientList[0], self.clientList[1])

        client_socket.close()
        server_socket.close()



s = Server("127.0.0.1", 12345)
s.run()