import socket
import json

# Paramètres du client
host = "127.0.0.1"  # Adresse IP du serveur
port = 12345  # Port du serveur

# Création d'une socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((host, port))

# Recevoir la demande de choix du serveur
message = client_socket.recv(1024).decode("utf-8")
print(message)

# Demander au joueur de choisir un mode
mode_choice = input("Votre choix (PVP ou solo): ")

# Envoyer la réponse au serveur
client_socket.send(mode_choice.encode("utf-8"))

# saisie du pseudo
pseudo = input("Votre pseudo : ")

# Envoyer la réponse au serveur
client_socket.send(pseudo.encode("utf-8"))

# Recevoir le plateau du joueur
message = client_socket.recv(1024).decode("utf-8")
print(message)

# Fermer la socket client
client_socket.close()
