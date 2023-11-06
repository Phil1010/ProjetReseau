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

bateauInput = input("ou mettre petit bateau ? (x, y, orientation)")
bateauValues = bateauInput.split(",")
bateau = Ship(bateauValues[0], bateauValues[1], 1, bateauValues[2])
print(ShipEncoder().encode(bateau))
client_socket.send(ShipEncoder().encode(bateau).encode())


bateauInput = input("ou mettre moyen bateau")
bateauValues = bateauInput.split(",")
bateau = Ship(bateauValues[0], bateauValues[1], 2, bateauValues[2])
print(ShipEncoder().encode(bateau))

client_socket.send(ShipEncoder().encode(bateau).encode())

bateauInput = input("ou mettre grand bateau")
bateauValues = bateauInput.split(",")
bateau = Ship(bateauValues[0], bateauValues[1], 3, bateauValues[2])
client_socket.send(ShipEncoder().encode(bateau).encode())

while True:
    message = client_socket.recv(2048).decode()
    if message != "play":
       print(message)
       break
    print(client_socket.recv(2048).decode())  # affichage grille
    coords = input("ou tirer ? (x, y)")
    client_socket.send(coords.encode())

