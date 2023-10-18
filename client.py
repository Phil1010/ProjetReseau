import socket
import json
import board
import ship

b = board.Board()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.connect(('127.0.0.1', 5050))
shipX = input("Placer petit bateau x: ")
shipY = input("Placer petit bateau y: ")
my_socket.send(ship.ShipEncoder().encode(ship.Ship(shipX, shipY, 2)).encode())
data = my_socket.recv(1024)
j = json.loads(data.decode())

b.grid = j
b.ship_little = [ship.Ship(shipX, shipY, 2)]
b.display()

my_socket.close()

