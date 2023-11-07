from http import client
from socket import socket, AF_INET, SOCK_STREAM
from games.MultiplayerGame import MultiplayerGame
from games.SoloGame import SoloGame
from player.Human import Human

class Server():
    def __init__(self, host, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((host, port))

        self.clientList = []

    def run(self):
        self.socket.listen(2)
        while True:
            client_socket, client_address = self.socket.accept()
            self.clientList.append(client_socket)
            print(len(self.clientList))
            if len(self.clientList) == 2:
                self.pvp(self.clientList[0], self.clientList[1])

        client_socket.close()
        server_socket.close()


    def pvp(self, clientASocket: socket, clientBSocket: socket):
        humanA = Human(clientASocket)
        humanB = Human(clientBSocket)
        game = MultiplayerGame(humanA, humanB)

        while not game.isFinished():
            game.nextTurn()


    def solo(self, client_socket):
        human = Human(client_socket)
        game = SoloGame(human)

        while not game.isFinished():
            game.nextTurn()


s = Server("127.0.0.1", 12345)
s.run()