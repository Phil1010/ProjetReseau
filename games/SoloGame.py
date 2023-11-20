from threading import Thread
from player.Bot import Bot
from player.Human import Human
from games.Game import Game
from player.Player import Player

class SoloGame(Game, Thread):
    def __init__(self, human: Human, bot: Player):
        super().__init__(human, bot)
