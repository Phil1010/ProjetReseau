import socket
import player
import board
import json

# Paramètres du serveur
host = "127.0.0.1"  # Adresse IP du serveur
port = 12345  # Port d'écoute du serveur

# Création d'une socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Liaison de la socket à l'adresse et au port
server_socket.bind((host, port))

# Attente de connexions
server_socket.listen(1)

print("Attente de connexions...")

# Accepter la connexion d'un client
client_socket, client_address = server_socket.accept()
print(f"Connexion établie avec {client_address}")

# Envoyer la demande de choix au client
client_socket.send("Choisissez votre mode de jeu (PVP ou solo): ".encode("utf-8"))

# Recevoir la réponse du client
mode_choice = client_socket.recv(1024).decode("utf-8")

if mode_choice.lower() == "pvp":
    print("Le client a choisi le mode PVP.")
    # Insérer ici le code pour le mode PVP
elif mode_choice.lower() == "solo":
    print("Le client a choisi le mode solo.")
    # le serveur reçoit le pseudo du joueur
    message = client_socket.recv(1024).decode("utf-8")
    print(f"Pseudo du joueur : {message}")
    # le serveur crée un player avec le pseudo du joueur
    player1 = player.Player(message, board.Board())

    player1.board.display_init()

    player_board_json = json.dumps(player1.board.get_board())
    client_socket.send(player_board_json.encode("utf-8"))
    print(player_board_json)

else:
    print("Choix de mode invalide.")

# Fermer les sockets
client_socket.close()
server_socket.close()
