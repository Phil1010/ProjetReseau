from socket import socket
from games.Game import Game
from player.Human import Human


class MultiplayerGame(Game):
    def __init__(self, playerA: Human, playerB: Human):
        super().__init__(playerA, playerB)
