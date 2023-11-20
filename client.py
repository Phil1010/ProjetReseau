import pickle
import os
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

                elif message.action == "get difficulty":
                    self.socket.send(pickle.dumps(Message("set difficulty", input("Choisissez une difficulté : (f)acile, (m)oyen, (d)ifficile"))))

                elif message.action == "get shot":
                    x = input("Choissisez une position x (entre 0 et 9 inclus) : ")
                    y = input("Choisissez une position y (entre 0 et 9 inclus) : ")

                    if (x == "ameno" or y == "ameno"):
                        self.socket.send(pickle.dumps(Message("ameno", "ameno")))
                    else:
                        # si x et y ne sont pas des entiers entre 0 et 9 on redemande
                        while not x.isdigit() or not y.isdigit() or int(x) < 0 or int(x) > 9 or int(y) < 0 or int(y) > 9:
                            print("Veuillez entrer des valeurs correctes")
                            x = input("Choissisez une position x (entre 0 et 9 inclus) : ")
                            y = input("Choisissez une position y (entre 0 et 9 inclus) : ")
                            
                        self.socket.send(pickle.dumps(Message("set shot", pickle.dumps(Shot(int(x), int(y))))))

                elif message.action == "get boat":
                    size = int(message.content)
                    x = input("Choisissez une position x pour le bateau de taille " + str(size) + " (entre 0 et 9 inclus) : ")
                    y = input("Choisissez une position y pour le bateau de taille " + str(size) + " (entre 0 et 9 inclus) : ")
                    orientation = input("Choisissez une orientation : (h)orizontal ou (v)ertical pour le bateau de taille " + str(size) + " : ")
                    #  si x et y ne sont pas des entiers entre 0 et 9 on redemande
                    
                    self.socket.send(pickle.dumps(Message("set boat", pickle.dumps(Ship(x, y, size, orientation))))) 

                elif message.action == "set grid":
                   print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n", message.content.replace("* ", "🚢").replace("X ", "💥").replace("0", "0️⃣").replace("1", "1️⃣").replace("2", "2️⃣").replace("3", "3️⃣").replace("4", "4️⃣").replace("5", "5️⃣").replace("6", "6️⃣").replace("7", "7️⃣").replace("8", "8️⃣").replace("9", "9️⃣").replace("~ ", "🌊").replace("! ", "🧱").replace("- ", "💧"))

                elif message.action == "set chronometer":
                    print(f"La partie a duré : {message.content} SECONDES")

                elif message.action == "end game":
                    print(f"{message.content}, fin de la partie.")

                elif message.action == "exit":
                    exit()

                elif message.action == "set timeout":
                    self.timeout = True
                    print("Vous avez mis trop de temps a jouer !")

                else:
                    print(message.action, message.content)
                    
Client("127.0.0.1", 12345).start()

