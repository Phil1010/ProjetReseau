import socket

from ship import Ship, ShipEncoder


# Paramètres du client
host = "127.0.0.1"  # Adresse IP du serveur
port = 12345  # Port du serveur

# Création d'une socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
client_socket.connect((host, port))

# saisie du pseudo
pseudo = input("Votre pseudo : ")

# Envoyer la réponse au serveur
client_socket.send(pseudo.encode("utf-8"))

# choisir l'emplacement des bateaux

n = 1

def placeBoat(size: int):
    x = input(f"\tEntrez la position x de votre bateau (entre 0 et {9-size} inclus) : ")
    y = input(f"\tEntrez la position y de votre bateau (entre 0 et {9-size} inclus) : ")
    d = input("\tEntrez la direction de votre bateau ((h)orizontal ou (v)ertical ) :  ")
    bateau = Ship(x, y, size, d)
    client_socket.send(ShipEncoder().encode(bateau).encode())

while True:
    print("En attente de votre adversaire...")
    messages = client_socket.recv(2048).decode()
    for message in messages.split("\n"):
        if message == "small boat":
           placeBoat(2)

        elif message == "medium boat":
            placeBoat(3)

        elif message == "big boat":
            placeBoat(4)

        elif message == "play":
            print(client_socket.recv(2048).decode())  # affichage grille
            x = input("Entrez la position x ou vous souhaitez tirer : ")
            y = input("Entrez la position y ou vous souhaitez tirer : ")
            client_socket.send(f"{x}, {y}".encode())

        else:
            print(message)

    