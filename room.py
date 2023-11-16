from player.Human import Human


class Room():
    def __init__(self, id):
        self.id = id
        self.humans = []

    def addHuman(self, human: Human):
        if len(self.humans) > 2:
            raise Exception("trop d'humains dans la salle")
        
        self.humans.append(human)