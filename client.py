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

while True:
    print("En attente de votre adversaire...")
    messages = client_socket.recv(2048).decode()
    for message in messages.split("\n"):
        if message == "boat":
            if n == 1:
                print("Placement du petit bateau : ")
            elif n == 2:
                print("Placement du bateau moyen : ")
            else:
                print("Placement du grand bateau : ")

            x = input("\tEntrez la position x de votre bateau (entre 0 et 9 inclus) : ")
            y = input("\tEntrez la position y de votre bateau (entre 0 et 9 inclus) : ")
            d = input("\tEntrez la direction de votre bateau (h ou v ) :  ")
            bateau = Ship(x, y, n, d)
            client_socket.send(ShipEncoder().encode(bateau).encode())

        elif message == "play":
            print(client_socket.recv(2048).decode())  # affichage grille
            x = input("Entrez la position x ou vous souhaitez tirer : ")
            y = input("Entrez la position y ou vous souhaitez tirer : ")
            client_socket.send(f"{x}, {y}".encode())

        else:
            print(message)
