import socket

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
while not (mode_choice.lower() == "pvp" or mode_choice.lower() == "solo"):
    mode_choice = input("Votre choix (PVP ou solo): ")

# Envoyer la réponse au serveur
client_socket.send(mode_choice.encode("utf-8"))

# saisie du pseudo
pseudo = input("Votre pseudo : ")
while pseudo.strip() == "":
    pseudo = input("Votre pseudo : ")

# Envoyer la réponse au serveur
client_socket.send(pseudo.encode("utf-8"))

# Recevoir le plateau du joueur
message = client_socket.recv(1024).decode("utf-8")
print(message)

# Demander au joueur de placer ses bateaux
placement1 = input(
    "Entrez les coordonnées du premier bateau x;y;longueur du bateau;son orientation(0<=x&y<=9; longueur = (2,3,4); orientation = h ou v) ex: 0;0;2;h: "
)

# Envoyer la réponse au serveur
client_socket.send(placement1.encode("utf-8"))

# Recevoir et afficher le plateau du joueur
message = client_socket.recv(1024).decode("utf-8")
print(message)

# Demander au joueur de placer ses bateaux
placement2 = input(
    "Entrez les coordonnées du deuxième bateau x;y;longueur du bateau;son orientation(0<=x&y<=9; longueur = (2,3,4); orientation = h ou v) ex: 0;0;2;h: "
)

# Envoyer la réponse au serveur
client_socket.send(placement2.encode("utf-8"))

# Recevoir et afficher le plateau du joueur
message = client_socket.recv(1024).decode("utf-8")
print(message)

# Demander au joueur de placer ses bateaux
placement3 = input(
    "Entrez les coordonnées du troisième bateau x;y;longueur du bateau;son orientation(0<=x&y<=9; longueur = (2,3,4); orientation = h ou v) ex: 0;0;2;h: "
)

# Envoyer la réponse au serveur
client_socket.send(placement3.encode("utf-8"))

# Recevoir et afficher le plateau du joueur
message = client_socket.recv(1024).decode("utf-8")
print("Voici votre plateau :" + "\n" + message)

# tant que le serveur n'a pas dit que le joueur a gagné ou le bot n'a pas gagné on continue la partie
while True:
    # Recevoir le plateau du bot
    message = client_socket.recv(1024).decode("utf-8")
    print("Voici le plateau de votre opposant : " + "\n" + message)

    # demande au joueur de tirer
    shot = input("Entrez les coordonnées du tir x;y (0<=x&y<=9): ")

    # Envoyer la réponse au serveur
    client_socket.send(shot.encode("utf-8"))

    # Recevoir le plateau du bot
    message = client_socket.recv(1024).decode("utf-8")
    print("Voici le plateau de votre opposant : " + "\n" + message)

    print("Votre ennemi a tiré !" + "\n" + "Voici votre plateau : ")
    message = client_socket.recv(1024).decode("utf-8")
    print(message)

    if "Vous avez gagné !" in message:
        break
    elif "Vous avez perdu !" in message:
        break


# Fermer la socket client
client_socket.close()
