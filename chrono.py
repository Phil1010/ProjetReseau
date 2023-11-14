from threading import Thread,Event
import time
from player.Human import Human


class Timer(Thread):
    def __init__(self, duration: int):
        super().__init__()
        self.duration = duration

    def run(self):
        while self.duration != 0:
            time.sleep(1)
            self.duration -= 1

        print("timer terminé")
        

class Chronometre(Thread):
    def __init__(self, human: Human, stop: Event):
        super().__init__()
        self.human = human
        self.stop = stop
        self.timer = 0

    def run(self):
        while not self.stop.is_set():
            time.sleep(1)
            self.timer += 1
            
        self.human.duration(self.timer)