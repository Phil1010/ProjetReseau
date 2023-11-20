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
                    print(self.timeout, "test")
                    x = input("Choissisez une position x : ")
                    y = input("Choisissez une position y : ")
                    # si x et y ne sont pas des entiers entre 0 et 9 on redemande
                    while not x.isdigit() or not y.isdigit() or int(x) < 0 or int(x) > 9 or int(y) < 0 or int(y) > 9:
                        print("Veuillez entrer des valeurs correctes")
                        x = input("Choissisez une position x : ")
                        y = input("Choisissez une position y : ")
                        

                   
                    self.socket.send(pickle.dumps(Message("set shot", pickle.dumps(Shot(int(x), int(y))))))

                elif message.action == "get boat":
                    size = int(message.content)
                    x = input("Choisissez une position x pour le bateau de taille " + str(size) + " : ")
                    y = input("Choisissez une position y pour le bateau de taille " + str(size) + " : ")
                    orientation = input("Choisissez une orientation " + str(size) + " : ")
                    #  si x et y ne sont pas des entiers entre 0 et 9 on redemande
                    
                    self.socket.send(pickle.dumps(Message("set boat", pickle.dumps(Ship(x, y, size, orientation))))) 

                elif message.action == "set grid":
                   print(message.content.replace("* ", "🚢").replace("X ", "💥").replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣").replace("~ ", "💧").replace("! ", "🧱"))

                elif message.action == "set chronometer":
                    print(f"La partie a duré : {message.content}")

                elif message.action == "set timeout":
                    self.timeout = True
                    print("Vous avez mis trop de temps a jouer !")

                else:
                    print("ERREUR", message.action, message.content)
                    
Client("192.168.246.126", 12345).start()

