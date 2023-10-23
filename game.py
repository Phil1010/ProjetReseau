from board import Board
from player import Player
from ship import Ship
from bot import Bot
import socket

class Game:
    def __init__(self, socket: socket.socket, player: Player):
        self.socket = socket
        self.player = player
        self.bot = Bot(Board())

    def sendBoard(self):
        self.socket.send(self.player.board.display_init().encode())

    def recvPlayerBoat(self):
        message = self.socket.recv(1024).decode("utf-8")

        x, y, size, direction = message.split(";")
        ship1 = Ship(int(x), int(y), int(size), direction)
        self.player.board.ships.append(ship1)
        self.player.board.add_ship(ship1)
        # le serveur envoie le plateau de départ au joueur
        self.socket.send(self.player.board.display_init().encode("utf-8"))

    def recvBotBoats(self):
        self.bot.add_ship_bot()
        self.bot.add_ship_bot()
        self.bot.add_ship_bot()

    