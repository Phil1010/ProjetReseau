import pickle
import socket
from threading import Thread
from message import Message
from shot import Shot
import random
from ship import Ship

class Client(Thread):
    def __init__(self, host: str, port: int):
        super().__init__()
        self.host = host
        self.port = port
        self.timeout = False

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        while True:
            messagesBytes = self.socket.recv(2048)

            for messageBytes in messagesBytes.split("\r\n".encode()):
                if len(messageBytes) == 0:
                    break

                message = pickle.loads(messageBytes)

                if message.action == "get username":
                    self.socket.send(pickle.dumps(Message("set username", input("Choisissez un nom d'utilisateur : "))) + "\r\n".encode())

                elif message.action == "get gamemode":
                    self.socket.send(pickle.dumps(Message("set gamemode", input("Choisissez un mode de jeu : (s)olo, (m)ultijoueur : ")))+ "\r\n".encode())

                elif message.action == "get room":
                    self.socket.send(pickle.dumps(Message("set room", input("Vous voulez (c)réer une salle ou un (r)ejoindre une ?"))))

                elif message.action == "show room": # affiche une room
                    print(pickle.loads(message.content)) # affichage de la liste des rooms

                elif message.action == "create room": # créer un room
                    self.socket.send(pickle.dumps(Message("set room", input("Entrez le nom de la room à créer : "))))

                elif message.action == "join room": # rejoindre une room
                    self.socket.send(pickle.dumps(Message("join room", input("Entrez le nom de la room à rejoindre : "))))

                elif message.action == "get shot":
                    x = input("Choissisez une position x : ")
                    y = input("Choisissez une position y : ")

                    if self.timeout:
                        print("Vous avez mis trop de temps a jouer !")
                        x = random.randint(0, 9) 
                        y = random.randint(0, 9)
                        self.timeout = False
                    self.socket.send(pickle.dumps(Message("set shot", pickle.dumps(Shot(int(x), int(y))))))

                elif message.action == "get boat":
                    size = int(message.content)
                    x = input("Choisissez une position x pour le bateau de taille " + str(size))
                    y = input("Choisissez une position y pour le bateau de taille " + str(size))
                    orientation = input("Choisissez une orientation " + str(size))
                    self.socket.send(pickle.dumps(Message("set boat", pickle.dumps(Ship(int(x), int(y), size, orientation))))) 

                elif message.action == "set grid":
                    print(message.content)

                elif message.action == "set chronometer":
                    print(f"La partie a duré : {message.content}")

                elif message.action == "set timeout":
                    self.timeout = True

                else:
                    print("ERREUR", message.action, message.content)
                    
Client("127.0.0.1", 12345).start()

