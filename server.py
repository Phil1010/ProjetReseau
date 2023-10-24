import socket
from player import Player
from board import Board
import json
import ship
from bot import Bot
from game import Game

# Paramètres du serveur
host = "127.0.0.1"  # Adresse IP du serveur
port = 12345  # Port d'écoute du serveur

# Création d'une socket serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def pvp(client_socket):
    print("Le client a choisi le mode PVP.")
    raise Exception("pvp not implemented")


def solo(client_socket):
    print("Le client a choisi le mode solo.")

    # le serveur reçoit le pseudo du joueur
    username = client_socket.recv(1024).decode("utf-8")
    print(f"Pseudo du joueur : {username}")

    # le serveur crée un player avec le pseudo du joueur
    player = Player(username, Board())

    game = Game(client_socket, player)

    # le serveur envoie le plateau de départ au joueur
    # client_socket.send(player.board.display_init().encode("utf-8"))
    game.sendBoard()

    # le serveur recoit la liste des placements des bateaux du joueur
    # message = client_socket.recv(1024).decode("utf-8")

    # le serveur va ajouter le bateau du joueur dans le plateau
    # x, y, size, direction = message.split(";")
    # ship1 = ship.Ship(int(x), int(y), int(size), direction)
    # player.board.ships.append(ship1)
    # player.board.add_ship(ship1)
    # # le serveur envoie le plateau de départ au joueur
    # client_socket.send(player.board.display_init().encode("utf-8"))

    # TODO: la fonction recvBoat recoit les 3 boats d'un coup
    game.recvPlayerBoat()  # recoit bateau 1

    # message = client_socket.recv(1024).decode("utf-8")
    # x2, y2, size2, direction2 = message.split(";")
    # ship2 = ship.Ship(int(x2), int(y2), int(size2), direction2)
    # player.board.ships.append(ship2)
    # player.board.add_ship(ship2)
    # client_socket.send(player.board.display_init().encode("utf-8"))
    game.recvPlayerBoat()  # recoit bateau 2

    # message = client_socket.recv(1024).decode("utf-8")
    # x3, y3, size3, direction3 = message.split(";")
    # ship3 = ship.Ship(int(x3), int(y3), int(size3), direction3)
    # player.board.ships.append(ship3)
    # player.board.add_ship(ship3)
    # client_socket.send(player.board.display_init().encode("utf-8"))
    game.recvPlayerBoat()  # recoit bateau 3

    # le serveur créer un bot
    # bot.Bot()
    # bot = bot.Bot(board.Board())
    # bot.add_ship_bot()
    # bot.add_ship_bot()
    # bot.add_ship_bot()
    game.recvBotBoats()  # recoit les bateaux du bot

    while True:
        print("Voici le plateau du bot : " + "\n" + game.bot.board.display_board())

        # le serveur envoi le plateau sans ship du bot au joueur
        client_socket.send(game.bot.board.display_board_without_ships().encode("utf-8"))

        # recevoir les coordonnées du tir du joueur
        print("Attente des coordonnées du tir du joueur...")
        message = client_socket.recv(1024).decode("utf-8")
        x, y = message.split(";")
        game.bot.board.shot(int(x), int(y))

        # envoyer le plateau du bot au joueur
        client_socket.send(game.bot.board.display_board_without_ships().encode("utf-8"))

        # le bot va tirer sur le joueur
        bot_shot = game.bot.shot()
        game.player.board.shot(bot_shot[0], bot_shot[1])
        print("Le bot a tiré sur les coordonnées : " + str(bot_shot))

        # envoyer le nouveau plateau du joueur au joueur
        print("envoie les coords au joueur")
        client_socket.send(game.player.board.display_board().encode("utf-8"))

        if game.player.board.is_win():
            client_socket.send("Vous avez perdu !".encode("utf-8"))
            print("Fin de la partie, le bot a gagner !")
            break
        elif game.bot.board.is_win():
            client_socket.send("Vous avez gagné !".encode("utf-8"))
            print("Fin de la partie, le joueur a gagner !")
            break


def run():
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
        pvp(client_socket)
    elif mode_choice.lower() == "solo":
        print("Le client a choisi le mode solo.")
        solo(client_socket)

    else:
        print("Choix de mode invalide.")
        # Recevoir la réponse du client
        mode_choice = client_socket.recv(1024).decode("utf-8")
        if mode_choice.lower() == "pvp":
            pvp(client_socket)

        elif mode_choice.lower() == "solo":
            solo(client_socket)

        else:
            print("Choix de mode invalide.")

    # Fermer les sockets
    client_socket.close()
    server_socket.close()


run()
