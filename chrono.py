from threading import Thread,Event
import time
from player.Human import Human
from player.Player import Player


class Timer(Thread):
    def __init__(self, player: Player, duration: int, stop: Event, spectators):
        super().__init__()
        self.duration = duration
        self.player = player
        self.stop = stop
        self.spectators = spectators

    def run(self):
        print("début timer ")
        while not self.stop.is_set() and self.duration != 0:
            time.sleep(1)
            self.duration -= 1
            if self.duration % 10 == 0 or self.duration <= 5:
                self.player.set_time(self.duration)
                for spectator in self.spectators:
                    spectator.set_time(self.duration)
            
        if not self.stop.is_set():
            self.player.timeout() 

class Chronometre(Thread):
    def __init__(self, playerA, playerB: Player, stop: Event):
        super().__init__()
        self.playerA = playerA
        self.playerB = playerB
        self.stop = stop
        self.timer = 0

    def run(self):
        while not self.stop.is_set():
            time.sleep(1)
            self.timer += 1
            
        self.playerA.notify(self.timer)
        self.playerB.notify(self.timer)
