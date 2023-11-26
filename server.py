from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
from typing import List
from games.MultiplayerGame import MultiplayerGame
from games.SoloGame import SoloGame
from player.BotMoyen import BotMoyen
from player.Bot import Bot
from player.Human import Human
from player.Player import Player
from player.Spectator import Spectator
from games.Game import Game


class HandleClient(Thread):
    def __init__(self, client_socket: socket, playerList: List, room_list, game_list):
        super().__init__()
        self.playerList = playerList
        self.room_list = room_list
        self.client_socket = client_socket
        self.game_list = game_list

    def pvp(self, humanA, humanB: Human) -> Game:
        return MultiplayerGame(humanA, humanB)

    def solo(self, human: Human, bot: Player) -> Game:
        return SoloGame(human, bot)

    def run(self):
        self.human = Human(self.client_socket)
        self.human.name = self.human.get_username()
        self.playerList.append(self.human)

        gamemode = self.human.get_gamemode()

        if gamemode == "s":
            difficulty = self.human.get_difficulty()
            if difficulty == "f":
                self.solo(self.human, Bot()).start()
            elif difficulty == "m":
                self.solo(self.human, BotMoyen()).start()

        elif gamemode == "m":
            room = self.human.get_room()
            if room == "c":
                room_name = self.human.create_room(self.room_list)
                self.room_list[room_name] = [self.human]

            elif room == "r":
                room_name = self.human.join_room(self.room_list)
                if len(self.room_list[room_name]) < 2:
                    self.room_list[room_name].append(self.human)

                    self.game_list[room_name] = self.pvp(
                        self.room_list[room_name][0], self.room_list[room_name][1]
                    )
                    self.game_list[room_name].start()

                elif len(self.room_list[room_name]) >= 2:
                    spectator = Spectator(self.client_socket)
                    self.game_list[room_name].spectators.append(spectator)


class Server:
    def __init__(self, host, port):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind((host, port))
        self.clientList = []
        self.room_list = {}
        self.game_list = {}

    def run(self):
        self.socket.listen(2)
        while True:
            client_socket, client_address = self.socket.accept()
            handler = HandleClient(
                client_socket, self.clientList, self.room_list, self.game_list
            )
            handler.start()

        client_socket.close()
        server_socket.close()


s = Server("127.0.0.1", 12345)
s.run()
