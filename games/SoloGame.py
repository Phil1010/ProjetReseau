import pickle
from re import I
from threading import Thread
from message import Message
from player.Bot import Bot
from player.Human import Human
from player.Player import Player
from games.Game import Game


class SoloGame(Game, Thread):
    def __init__(self, human: Human):
        super().__init__(human, Bot())