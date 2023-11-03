import socket
from games.SoloGame import SoloGame
from player.Human import Human

# Paramètres du serveur
host = "127.0.0.1"  # Adresse IP du serveur
port = 12345  # Port d'écoute du serveur

# Création d'une socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def pvp(client_socket):
    print("Le client a choisi le mode PVP.")
    raise Exception("pvp not implemented")


def solo(client_socket):
    human = Human(client_socket)
    game = SoloGame(human)

    while not game.isFinished():
        game.nextTurn()


def run():
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Attente de connexions...")

    client_socket, client_address = server_socket.accept()
    print(f"Connexion établie avec {client_address}")

    solo(client_socket)

    # # Envoyer la demande de choix au client
    # client_socket.send("Choisissez votre mode de jeu (PVP ou solo): ".encode("utf-8"))

    # # Recevoir la réponse du client
    # mode_choice = client_socket.recv(1024).decode("utf-8")

    # if mode_choice.lower() == "pvp":
    #     print("Le client a choisi le mode PVP.")
    #     pvp(client_socket)
    # elif mode_choice.lower() == "solo":
    #     print("Le client a choisi le mode solo.")
    #     solo(client_socket)

    # else:
    #     print("Choix de mode invalide.")
    #     # Recevoir la réponse du client
    #     mode_choice = client_socket.recv(1024).decode("utf-8")
    #     if mode_choice.lower() == "pvp":
    #         pvp(client_socket)

    #     elif mode_choice.lower() == "solo":
    #         solo(client_socket)

    #     else:
    #         print("Choix de mode invalide.")

    # Fermer les sockets
    client_socket.close()
    server_socket.close()


run()
