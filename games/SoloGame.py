from games.Game import Game
from player.Bot import Bot
from player.Player import Player


class SoloGame(Game):
    def __init__(self, player: Player):
        super().__init__(player, Bot())
