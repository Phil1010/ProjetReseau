from threading import Thread
from player.Bot import Bot
from player.Human import Human
from games.Game import Game


class SoloGame(Game, Thread):
    def __init__(self, human: Human):
        super().__init__(human, Bot())
