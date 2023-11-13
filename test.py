from threading import Thread
import threading
import time



class Reader(Thread):
    def __init__(self, event: threading.Event):
        super().__init__()
        self.event = event

    def run(self):
        while not self.event.is_set():
            pass

        print("temps écoulé")

class Writer(Thread):
    def __init__(self, event: threading.Event):
        super().__init__()
        self.event = event

    def run(self):
        while not self.event.is_set():
            input("input ?")
            self.event.set()

event = threading.Event()
Writer(event).start()
Reader(event).start()



