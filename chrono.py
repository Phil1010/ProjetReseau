from threading import Thread
import time


class Timer(Thread):
    def __init__(self, duration: int):
        super().__init__()
        self.duration = duration

    def run(self):
        while self.duration != 0:
            time.sleep(1)
            self.duration -= 1

        print("timer terminé")